const raws = [
  "raw-ase-spec",
  "raw-br-immed-retired",
  "raw-br-immed-spec",
  "raw-br-indirect-spec",
  "raw-br-mis-pred",
  "raw-br-mis-pred-retired",

  "raw-br-pred",
  "raw-br-retired",
  "raw-br-return-retired",
  "raw-br-return-spec",
  "raw-bus-access",
  "raw-bus-access-normal",

  "raw-bus-access-not-shared",
  "raw-bus-access-periph",
  "raw-bus-access-rd",
  "raw-bus-access-shared",
  "raw-bus-access-wr",
  "raw-bus-cycles",

  "raw-chain", // ????????????
  "raw-cid-write-retired",
  "raw-cnt-cycles",
  "raw-cpu-cycles",
  "raw-crypto-spec",
  "raw-dmb-spec",

  "raw-dp-spec",
  "raw-dsb-spec",
  "raw-dtlb-walk",
  "raw-exc-dabort",
  "raw-exc-fiq",
  "raw-exc-hvc",

  "raw-exc-irq",
  "raw-exc-pabort",
  "raw-exc-return",
  "raw-exc-smc",
  "raw-exc-svc",
  "raw-exc-taken",

  "raw-exc-trap-dabort",
  "raw-exc-trap-fiq",
  "raw-exc-trap-irq",
  "raw-exc-trap-other",
  "raw-exc-trap-pabort",
  "raw-exc-undef",

  "raw-inst-retired",
  "raw-inst-spec",
  "raw-isb-spec",
  "raw-itlb-walk",
  "raw-l1d-cache",
  "raw-l1d-cache-allocate",

  "raw-l1d-cache-inval",
  "raw-l1d-cache-lmiss-rd",
  "raw-l1d-cache-rd",
  "raw-l1d-cache-refill",
  "raw-l1d-cache-refill-inner",
  "raw-l1d-cache-refill-outer",

  "raw-l1d-cache-refill-rd",
  "raw-l1d-cache-refill-wr",
  "raw-l1d-cache-wb",
  "raw-l1d-cache-wb-clean",
  "raw-l1d-cache-wb-victim",
  "raw-l1d-cache-wr",

  "raw-l1d-tlb",
  "raw-l1d-tlb-rd",
  "raw-l1d-tlb-refill",
  "raw-l1d-tlb-refill-rd",
  "raw-l1d-tlb-refill-wr",
  "raw-l1d-tlb-wr",

  "raw-l1i-cache",
  "raw-l1i-cache-lmiss",
  "raw-l1i-cache-refill",
  "raw-l1i-tlb",
  "raw-l1i-tlb-refill",
  "raw-l2d-cache",

  "raw-l2d-cache-allocate",
  "raw-l2d-cache-inval",
  "raw-l2d-cache-lmiss-rd",
  "raw-l2d-cache-rd",
  "raw-l2d-cache-refill",
  "raw-l2d-cache-refill-rd",

  "raw-l2d-cache-refill-wr",
  "raw-l2d-cache-wb",
  "raw-l2d-cache-wb-clean",
  "raw-l2d-cache-wb-victim",
  "raw-l2d-cache-wr",
  "raw-l2d-tlb",

  "raw-l2d-tlb-rd",
  "raw-l2d-tlb-refill",
  "raw-l2d-tlb-refill-rd",
  "raw-l2d-tlb-refill-wr",
  "raw-l2d-tlb-wr",
  "raw-l2i-cache",

  "raw-l2i-cache-lmiss",
  "raw-l2i-cache-refill",
  "raw-l2i-tlb",
  "raw-l2i-tlb-refill",
  "raw-l3d-cache",
  "raw-l3d-cache-allocate",

  "raw-l3d-cache-inval",
  "raw-l3d-cache-lmiss-rd",
  "raw-l3d-cache-rd",
  "raw-l3d-cache-refill",
  "raw-l3d-cache-refill-rd",
  "raw-l3d-cache-refill-wr",

  "raw-l3d-cache-wb",
  "raw-l3d-cache-wb-clean",
  "raw-l3d-cache-wb-victim",
  "raw-l3d-cache-wr",
  "raw-ld-retired",
  "raw-ld-spec",

  "raw-ldrex-spec",
  "raw-ldst-spec",
  "raw-ll-cache",
  "raw-ll-cache-miss",
  "raw-ll-cache-miss-rd",
  "raw-ll-cache-rd",

  "raw-mem-access",
  "raw-mem-access-rd",
  "raw-mem-access-wr",
  "raw-memory-error",
  "raw-op-retired",
  "raw-op-spec",

  "raw-pc-write-retired",
  "raw-pc-write-spec",
  "raw-rc-ld-spec",
  "raw-rc-st-spec",
  "raw-remote-access",
  "raw-remote-access-rd",

  "raw-sample-collision",
  "raw-sample-feed",
  "raw-sample-filtrate",
  "raw-sample-pop",
  "raw-st-retired",
  "raw-st-spec",

  "raw-stall",
  "raw-stall-backend",
  "raw-stall-backend-mem",
  "raw-stall-frontend",
  "raw-stall-slot",
  "raw-stall-slot-backend",

  "raw-stall-slot-frontend",
  "raw-strex-fail-spec",
  "raw-strex-pass-spec",
  "raw-strex-spec",
  "raw-sve-inst-retired",
  "raw-sve-inst-spec",

  "raw-sw-incr",
  "raw-ttbr-write-retired",
  "raw-unaligned-ld-spec",
  "raw-unaligned-ldst-retired",
  "raw-unaligned-ldst-spec",
  "raw-unaligned-st-spec",

  "raw-vfp-spec",
];
