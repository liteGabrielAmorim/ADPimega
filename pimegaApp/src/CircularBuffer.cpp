#include "CircularBuffer.h"

CircularBuffer::CircularBuffer(size_t numBuffers, size_t sizex, size_t sizey,
                               NDDataType_t dtype, NDArrayPool *pool)
    : currentIndex(0) {
  size_t array_dims[2] = {sizex, sizey};
  for (size_t i = 0; i < numBuffers; ++i) {
    NDArray *array = pool->alloc(2, array_dims, dtype, 0, nullptr);
    buffer.push_back(array);
  }
}

CircularBuffer::~CircularBuffer() { clear(); }

NDArray *CircularBuffer::getNext() {
  NDArray *array = buffer[currentIndex];
  currentIndex = (currentIndex + 1) % buffer.size();
  return array;
}

void CircularBuffer::clear() {
  for (auto array : buffer) {
    if (array) {
      array->release();
    }
  }
  buffer.clear();
}

size_t CircularBuffer::size() const { return buffer.size(); }
