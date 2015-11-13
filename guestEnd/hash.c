#include <linux/module.h>    
#include <linux/kernel.h>   
#include <linux/init.h>      
#include <linux/mm.h>
#include <linux/bootmem.h>
#include <asm/page_64.h>
#include <asm/page.h>
#include <asm/mmzone.h>
#include <linux/mmzone.h>
#include <linux/mm_types.h>

#include <linux/fs.h>
#include <asm/segment.h>
#include <asm/uaccess.h>
#include <linux/buffer_head.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Deependra Patel");
MODULE_DESCRIPTION("Module to calculate hash of entire physical memory and write to file");

struct file* logFile;
//extern unsigned long max_pfn;

#undef get16bits
#if (defined(__GNUC__) && defined(__i386__)) || defined(__WATCOMC__) \
  || defined(_MSC_VER) || defined (__BORLANDC__) || defined (__TURBOC__)
#define get16bits(d) (*((const uint16_t *) (d)))
#endif

#if !defined (get16bits)
#define get16bits(d) ((((uint32_t)(((const uint8_t *)(d))[1])) << 8)\
                       +(uint32_t)(((const uint8_t *)(d))[0]) )
#endif

//SuperFastHash doesn't belong to me
uint32_t SuperFastHash (const char * data, int len) {
uint32_t hash = len, tmp;
int rem;

    if (len <= 0 || data == NULL) return 0;

    rem = len & 3;
    len >>= 2;

    /* Main loop */
    for (;len > 0; len--) {
        hash  += get16bits (data);
        tmp    = (get16bits (data+2) << 11) ^ hash;
        hash   = (hash << 16) ^ tmp;
        data  += 2*sizeof (uint16_t);
        hash  += hash >> 11;
    }

    /* Handle end cases */
    switch (rem) {
        case 3: hash += get16bits (data);
                hash ^= hash << 16;
                hash ^= ((signed char)data[sizeof (uint16_t)]) << 18;
                hash += hash >> 11;
                break;
        case 2: hash += get16bits (data);
                hash ^= hash << 11;
                hash += hash >> 17;
                break;
        case 1: hash += (signed char)*data;
                hash ^= hash << 10;
                hash += hash >> 1;
    }

    /* Force "avalanching" of final 127 bits */
    hash ^= hash << 3;
    hash += hash >> 5;
    hash ^= hash << 4;
    hash += hash >> 17;
    hash ^= hash << 25;
    hash += hash >> 6;

    return hash;
}

struct file* file_open(const char* path, int flags, int rights) {
    struct file* filp = NULL;
    mm_segment_t oldfs;
    int err = 0;
    printk("Opening file\n");
    oldfs = get_fs();
    set_fs(get_ds());
    filp = filp_open(path, flags, rights);
    set_fs(oldfs);
    if(IS_ERR(filp)) {
        err = PTR_ERR(filp);
        return NULL;
    }
    printk("Opened file");
    return filp;
}
int file_write(struct file* file, unsigned long long offset, unsigned char* data, unsigned int size) {
    mm_segment_t oldfs;
    int ret;

    oldfs = get_fs();
    set_fs(get_ds());

    ret = vfs_write(file, data, size, &offset);

    set_fs(oldfs);
    return ret;
}

int file_sync(struct file* file) {
    vfs_fsync(file, 0);
    return 0;
}
void file_close(struct file* file) {
    filp_close(file, NULL);
}

void write_hash_to_file(int i, unsigned char* data){
  uint32_t hashed = SuperFastHash(data, PAGE_SIZE);
  //file_write(logFile, i*4096, data, 4096); 
  unsigned char charHash[4];
  charHash[0] = hashed>>24;
  charHash[1] = hashed>>16;
  charHash[2] = hashed>>8;
  charHash[3] = hashed;
  /*if(i<10){
    printk("i=%d Hash %u", i, hashed);
    printk(" Character hash %c %c %c %c\n", charHash[0], charHash[1], charHash[2], charHash[3]);
  }*/
  file_write(logFile, i*4, charHash, 4);
}

static int __init hello_init(void)
{
  int i, total, countUsedPage;
  struct page* curPage;

  char path[] = "./hash.bin";
  printk(KERN_INFO "Starting module. You have %lu pages to play with!\n", get_num_physpages());
  logFile = file_open(path, O_CREAT | O_WRONLY, S_IRWXU);
  curPage = pfn_to_page(node_data[0]->node_start_pfn);
  total = get_num_physpages();
  countUsedPage = 0;
  for(i=0; i<total; i++){
      curPage = pfn_to_page(node_data[0]->node_start_pfn + i);
      if(page_count(curPage) > 0){
          write_hash_to_file(countUsedPage, kmap(curPage)); 
          countUsedPage++;
      }
  }
  file_sync(logFile);
  file_close(logFile);
  printk(KERN_INFO "Save the world! countUsedPage:%d\n", countUsedPage);
  return 0;
}

static void __exit hello_cleanup(void)
{
    printk(KERN_INFO "Cleaning up module. Bye!\n");
}

module_init(hello_init);
module_exit(hello_cleanup);
