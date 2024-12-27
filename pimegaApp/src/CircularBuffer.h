#ifndef CIRCULAR_BUFFER_H
#define CIRCULAR_BUFFER_H

#include <vector>

#include "ADDriver.h"

class CircularBuffer {
 public:
  CircularBuffer(size_t numBuffers, size_t sizex, size_t sizey,
                 NDDataType_t dtype, NDArrayPool *pool);
  ~CircularBuffer();
  NDArray *getNext();
  void clear();
  size_t size() const;

 private:
  std::vector<NDArray *> buffer;
  size_t currentIndex;
};

#endif  // CIRCULAR_BUFFER_H
