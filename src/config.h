#pragma once

namespace libra {

  typedef int graph_node_t;
  typedef long graph_edge_t;
  typedef char pattern_node_t;
  typedef unsigned char label_t;
  typedef char set_op_t;
  typedef unsigned int bitarray32;

  inline constexpr size_t PAT_SIZE = 8;
  inline constexpr size_t GRAPH_DEGREE = 4096;

  inline constexpr int GRID_DIM = 40;
  inline constexpr int BLOCK_DIM = 1024;
  inline constexpr int WARP_SIZE = 32;
  inline constexpr int NWARPS_PER_BLOCK = (BLOCK_DIM / WARP_SIZE);
  inline constexpr int NWARPS_TOTAL = ((GRID_DIM * BLOCK_DIM + WARP_SIZE - 1) / WARP_SIZE);

  // TODO: determine chunk size based on max_degree and tot number of jobs
  inline constexpr graph_node_t JOB_CHUNK_SIZE = 4;
  // static_assert(2 * JOB_CHUNK_SIZE <= GRAPH_DEGREE); 
}