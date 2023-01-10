# pmu

<!-- vim-markdown-toc GFM -->

* [Cortex A76](#cortex-a76)

<!-- vim-markdown-toc -->

## Cortex A76

```zsh
simpleperf list raw
```

| type              | num  | event                      | description                              | note                   | spec | hw  | zero | dup | filter |
| ----------------- | ---- | -------------------------- | ---------------------------------------- | ---------------------- | ---- | --- | ---- | --- | ------ |
| cycle             | 0x11 | raw-cpu-cycles             |                                          |                        |      |     |      |     |        |
|                   | 0x1D | raw-bus-cycles             | = -cpu-cycles                            |                        |      |     |      | x   | x      |
|                   |      | raw-cnt-cycles             |                                          |                        | x    |     | x    |     | x      |
| instr.            | 0x8  | raw-inst-retired           |                                          |                        |      |     |      |     |        |
| instr. branch     | 0x21 | raw-br-retired             |                                          | ⊆ -inst-retired        |      |     |      |     |        |
|                   | 0x22 | raw-br-mis-pred-retired    |                                          | ⊆ -br-retired          |      |     |      |     |        |
|                   |      | raw-br-immed-retired       |                                          | ⊆ -br-retired          | x    |     |      |     |        |
|                   |      | raw-br-return-retired      |                                          | ⊆ -br-retired          | x    |     |      |     |        |
| instr. load/store |      | raw-ld-retired             |                                          | ⊆ -inst-retired        | x    |     |      |     |        |
|                   |      | raw-st-retired             |                                          | ⊆ -inst-retired        | x    |     |      |     |        |
|                   |      | raw-unaligned-ldst-retired |                                          | ⊆ -inst-retired        | x    |     |      |     |        |
| instr. other      |      | raw-op-retired             |                                          | ⊆ -inst-retired        | x    |     | x    |     | x      |
|                   |      | raw-sve-inst-retired       |                                          | ⊆ -inst-retired        | x    |     | x    |     | x      |
|                   |      | raw-pc-write-retired       |                                          | ⊆ -inst-retired        | x    |     |      |     |        |
|                   | 0x0  | raw-sw-incr                |                                          | ⊆ -inst-retired        |      |     | x    |     |        |
|                   | 0x0A | raw-exc-return             |                                          | ⊆ -inst-retired        |      |     |      |     |        |
|                   | 0x0B | raw-cid-write-retired      |                                          | ⊆ -inst-retired        |      |     |      |     |        |
|                   | 0x1C | raw-ttbr-write-retired     |                                          | ⊆ -inst-retired        |      |     |      |     |        |
| op.               | 0x1B | raw-inst-spec              | ≈ -retired                               |                        |      |     |      | x   | x      |
| op. branch        | 0x12 | raw-br-pred                | ≈ -retired                               | ⊆ -inst-spec           |      |     |      | x   | x      |
|                   | 0x10 | raw-br-mis-pred            | ≈ -retired                               | ⊆ -br-pred             |      |     |      | x   | x      |
|                   | 0x78 | raw-br-immed-spec          | ≈ -retired                               | ⊆ -br-pred             |      |     |      | x   | x      |
|                   | 0x79 | raw-br-return-spec         | ≈ -retired                               | ⊆ -br-pred             |      |     |      | x   | x      |
|                   | 0x7A | raw-br-indirect-spec       |                                          | ⊆ -br-pred             |      |     |      |     |        |
| op. load/store    | 0x72 | raw-ldst-spec              | ≈ -retired = -ld-spec + -st-spec         | ⊆ -inst-spec           |      |     |      |     |        |
|                   | 0x70 | raw-ld-spec                | ≈ -retired                               | ⊆ -ldst-spec           |      |     |      | x   | x      |
|                   | 0x71 | raw-st-spec                | ≈ -retired                               | ⊆ -ldst-spec           |      |     |      | x   | x      |
|                   | 0x6A | raw-unaligned-ldst-spec    | ≈ -retired = -ld-spec + -st-spec         | ⊆ -inst-spec           |      |     | x    | ?   |        |
|                   | 0x68 | raw-unaligned-ld-spec      |                                          | ⊆ -unaligned-ldst-spec |      |     | x    |     |        |
|                   | 0x69 | raw-unaligned-st-spec      |                                          | ⊆ -unaligned-ldst-spec |      |     | x    |     |        |
| op. other         |      | raw-op-spec                | ≈ -retired                               | ⊆ -inst-spec           | x    |     | x    | x   | x      |
|                   |      | raw-sve-inst-spec          | ≈ -retired                               | ⊆ -inst-spec           | x    |     | x    | x   | x      |
|                   | 0x76 | raw-pc-write-spec          | ≈ -retired                               | ⊆ -inst-spec           |      |     |      | ?   |        |
|                   | 0x73 | raw-dp-spec                |                                          | ⊆ -inst-spec           |      |     |      |     |        |
|                   | 0x74 | raw-ase-spec               |                                          | ⊆ -inst-spec           |      |     |      |     |        |
|                   | 0x75 | raw-vfp-spec               |                                          | ⊆ -inst-spec           |      |     |      |     |        |
|                   | 0x77 | raw-crypto-spec            |                                          | ⊆ -inst-spec           |      |     |      |     |        |
|                   | 0x6C | raw-ldrex-spec             |                                          | ⊆ -inst-spec           |      |     | x    |     |        |
|                   | 0x6F | raw-strex-spec             | = -pass-spec + -fail-spec                | ⊆ -inst-spec           |      |     | x    |     |        |
|                   | 0x6D | raw-strex-pass-spec        |                                          | ⊆ -strex-spec          |      |     | x    |     |        |
|                   | 0x6E | raw-strex-fail-spec        |                                          | ⊆ -strex-spec          |      |     | x    |     |        |
|                   | 0x90 | raw-rc-ld-spec             |                                          | ⊆ -inst-spec           |      |     | x    |     |        |
|                   | 0x91 | raw-rc-st-spec             |                                          | ⊆ -inst-spec           |      |     | x    |     |        |
|                   | 0x7C | raw-isb-spec               |                                          | ⊆ -inst-spec           |      |     | x    |     |        |
|                   | 0x7D | raw-dsb-spec               |                                          | ⊆ -inst-spec           |      |     | x    |     |        |
|                   | 0x7E | raw-dmb-spec               |                                          | ⊆ -inst-spec           |      |     | x    |     |        |
| bus               | 0x19 | raw-bus-access             | -rd + -wr                                |                        |      |     |      |     |        |
|                   | 0x60 | raw-bus-access-rd          |                                          | ⊆ -bus-access          |      |     |      |     |        |
|                   | 0x61 | raw-bus-access-wr          |                                          | ⊆ -bus-access          |      |     |      |     |        |
|                   |      | raw-bus-access-normal      |                                          | ⊆ -bus-access          | x    |     | x    |     | x      |
|                   |      | raw-bus-access-shared      |                                          | ⊆ -bus-access          | x    |     | x    |     | x      |
|                   |      | raw-bus-access-not-shared  |                                          | ⊆ -bus-access          | x    |     | x    |     | x      |
|                   |      | raw-bus-access-periph      |                                          | ⊆ -bus-access          | x    |     | x    |     | x      |
| exception         | 0x9  | raw-exc-taken              |                                          |                        |      |     |      |     |        |
|                   | 0x81 | raw-exc-undef              |                                          | ⊆ -exc-taken           |      |     | x    |     |        |
|                   | 0x82 | raw-exc-svc                |                                          | ⊆ -exc-taken           |      |     | x    |     |        |
|                   | 0x83 | raw-exc-pabort             |                                          | ⊆ -exc-taken           |      |     | x    |     |        |
|                   | 0x8B | raw-exc-trap-pabort        |                                          | ⊆ -exc-pabort          |      |     | x    |     |        |
|                   | 0x84 | raw-exc-dabort             |                                          | ⊆ -exc-taken           |      |     | x    |     |        |
|                   | 0x8C | raw-exc-trap-dabort        |                                          | ⊆ -exc-dabort          |      |     | x    |     |        |
|                   | 0x86 | raw-exc-irq                |                                          | ⊆ -exc-taken           |      |     |      |     |        |
|                   | 0x8E | raw-exc-trap-irq           |                                          | ⊆ -exc-irq             |      |     | x    |     |        |
|                   | 0x87 | raw-exc-fiq                |                                          | ⊆ -exc-taken           |      |     |      |     |        |
|                   | 0x8F | raw-exc-trap-fiq           |                                          | ⊆ -exc-fiq             |      |     | x    |     |        |
|                   | 0x88 | raw-exc-smc                |                                          | ⊆ -exc-taken           |      |     | x    |     |        |
|                   | 0x8A | raw-exc-hvc                |                                          | ⊆ -exc-taken           |      |     | x    |     |        |
|                   | 0x8D | raw-exc-trap-other         |                                          | ⊆ -exc-taken           |      |     | x    |     |        |
| L1 I-Cache        | 0x14 | raw-l1i-cache              |                                          |                        |      |     |      |     |        |
|                   | 0x1  | raw-l1i-cache-refill       |                                          | ⊆ -l1i-cache           |      |     |      |     |        |
|                   |      | raw-l1i-cache-lmiss        |                                          | ⊆ -l1i-cache-refill    | x    |     | x    |     | x      |
| L1 I-Cache TLB    | 0x26 | raw-l1i-tlb                |                                          |                        |      |     |      |     |        |
|                   | 0x2  | raw-l1i-tlb-refill         |                                          | ⊆ -l1i-tlb             |      |     |      |     |        |
| L1 D-Cache        | 0x4  | raw-l1d-cache              | = -rd + -wr                              |                        |      |     |      |     |        |
|                   | 0x40 | raw-l1d-cache-rd           | (CPU <= L1) ⊇ -refill-rd                 | ⊆ -l1d-cache           |      |     |      |     |        |
|                   | 0x41 | raw-l1d-cache-wr           | write during store include -refill-wr    | ⊆ -l1d-cache           |      |     |      |     |        |
|                   |      | raw-l1d-cache-allocate     |                                          | ⊆ -l1d-cache-wr        | x    |     | x    |     | x      |
|                   | 0x3  | raw-l1d-cache-refill       | = L1 <= L2 = -rd + -wr = -inner + -outer | ⊆ -l1d-cache-wr        |      |     |      |     |        |
|                   | 0x44 | raw-l1d-cache-refill-inner | L1 miss, L2 and L3 hit                   | ⊆ -l1d-cache-refill    |      |     |      |     |        |
|                   | 0x45 | raw-l1d-cache-refill-outer | L1 miss, L2 or L3 miss                   | ⊆ -l1d-cache-refill    |      |     |      |     |        |
|                   | 0x42 | raw-l1d-cache-refill-rd    | L1 <= L2 during load                     | ⊆ -l1d-cache-refill    |      |     |      |     |        |
|                   |      | raw-l1d-cache-lmiss-rd     |                                          | ⊆ -l1d-cache-refill-rd | x    |     | x    |     | x      |
|                   | 0x43 | raw-l1d-cache-refill-wr    | write during store L1 <= L2 during store | ⊆ -l1d-cache-refill    |      |     |      |     |        |
|                   | 0x15 | raw-l1d-cache-wb           | L1 => L2                                 |                        |      |     |      |     |        |
|                   | 0x46 | raw-l1d-cache-wb-victim    |                                          | ⊆ -l1d-cache-wb        |      |     | x    |     |        |
|                   | 0x47 | raw-l1d-cache-wb-clean     |                                          | ⊆ -l1d-cache-wb        |      |     | x    |     |        |
|                   | 0x48 | raw-l1d-cache-inval        |                                          |                        |      |     | x    |     |        |
| L1 D-Cache TLB    | 0x25 | raw-l1d-tlb                | = -rd + -wr                              |                        |      |     |      |     |        |
|                   | 0x4E | raw-l1d-tlb-rd             |                                          | ⊆ -l1d-tlb             |      |     | x    |     |        |
|                   | 0x4F | raw-l1d-tlb-wr             |                                          | ⊆ -l1d-tlb             |      |     | x    |     |        |
|                   | 0x5  | raw-l1d-tlb-refill         | = -rd + -wr                              | ⊆ -l1d-tlb-wr          |      |     |      |     |        |
|                   | 0x4C | raw-l1d-tlb-refill-rd      |                                          | ⊆ -l1d-tlb-refill      |      |     | x    |     |        |
|                   | 0x4D | raw-l1d-tlb-refill-wr      |                                          | ⊆ -l1d-tlb-refill      |      |     | x    |     |        |
| L2 I-Cache        |      | raw-l2i-cache              |                                          |                        | x    |     | x    |     | x      |
|                   |      | raw-l2i-cache-refill       |                                          | ⊆ -l2i-cache           | x    |     | x    |     | x      |
|                   |      | raw-l2i-cache-lmiss        |                                          | ⊆ -l2i-cache-refill    | x    |     | x    |     | x      |
| L2 I-Cache TLB    |      | raw-l2i-tlb                |                                          |                        | x    |     | x    |     | x      |
|                   |      | raw-l2i-tlb-refill         |                                          | ⊆ -l2i-tlb             | x    |     | x    |     | x      |
| L2 D-Cache        | 0x16 | raw-l2d-cache              | = -rd + -wr                              |                        |      |     |      |     |        |
|                   | 0x50 | raw-l2d-cache-rd           | L1 <= L2                                 | ⊆ -l2d-cache           |      |     |      |     |        |
|                   | 0x51 | raw-l2d-cache-wr           | ≈ -l1d-cache-wb (L1 => L2)               | ⊆ -l2d-cache           |      |     |      |     |        |
|                   | 0x20 | raw-l2d-cache-allocate     | include -l1d-cache-wb                    | ⊆ -l2d-cache-wr        |      |     |      |     |        |
|                   | 0x17 | raw-l2d-cache-refill       | = -rd + -wr                              | ⊆ -l2d-cache-wr        |      |     |      |     |        |
|                   | 0x52 | raw-l2d-cache-refill-rd    |                                          | ⊆ -l2d-cache-refill    |      |     |      |     |        |
|                   |      | raw-l2d-cache-lmiss-rd     |                                          | ⊆ -l2d-cache-refill-rd | x    |     | x    |     |        |
|                   | 0x53 | raw-l2d-cache-refill-wr    |                                          | ⊆ -l2d-cache-refill    |      |     |      |     |        |
|                   | 0x18 | raw-l2d-cache-wb           | L2 => L3                                 |                        |      |     |      |     |        |
|                   | 0x56 | raw-l2d-cache-wb-victim    |                                          | ⊆ -l2d-cache-wb        |      |     | x    |     |        |
|                   | 0x57 | raw-l2d-cache-wb-clean     |                                          | ⊆ -l2d-cache-wb        |      |     | x    |     |        |
|                   | 0x58 | raw-l2d-cache-inval        |                                          |                        |      |     | x    |     |        |
| L2 D-Cache TLB    | 0x2F | raw-l2d-tlb                | = -rd + -wr                              |                        |      |     |      |     |        |
|                   | 0x5E | raw-l2d-tlb-rd             |                                          | ⊆ -l2d-tlb             |      |     | x    |     |        |
|                   | 0x5F | raw-l2d-tlb-wr             |                                          | ⊆ -l2d-tlb             |      |     | x    |     |        |
|                   | 0x2D | raw-l2d-tlb-refill         | = -rd + -wr                              | ⊆ -l2d-tlb-wr          |      |     |      |     |        |
|                   | 0x34 | raw-dtlb-walk              |                                          |                        |      |     |      |     |        |
|                   | 0x35 | raw-itlb-walk              |                                          |                        |      |     |      |     |        |
|                   | 0x5C | raw-l2d-tlb-refill-rd      |                                          | ⊆ -l2d-tlb-refill      |      |     | x    |     |        |
|                   | 0x5D | raw-l2d-tlb-refill-wr      |                                          | ⊆ -l2d-tlb-refill      |      |     | x    |     |        |
| L3 D-Cache        | 0x2B | raw-l3d-cache              | = -rd + -wr                              |                        |      |     |      |     |        |
|                   |      | raw-l3d-cache-rd           |                                          | ⊆ -l3d-cache           | x    |     |      |     |        |
|                   |      | raw-l3d-cache-wr           | ≈ -l2d-cache-wb (L2 => L3)               | ⊆ -l3d-cache           | x    |     | x    |     |        |
|                   | 0x29 | raw-l3d-cache-allocate     | ≈ -l3d-cache-wr                          | ⊆ -l3d-cache-wr        |      |     |      |     |        |
|                   | 0x2A | raw-l3d-cache-refill       | = -rd + -wr                              | ⊆ -l3d-cache-wr        |      |     |      |     |        |
|                   |      | raw-l3d-cache-refill-rd    |                                          | ⊆ -l3d-cache-refill    | x    |     |      |     |        |
|                   |      | raw-l3d-cache-lmiss-rd     |                                          | ⊆ -l3d-cache-refill-rd | x    |     | x    |     |        |
|                   |      | raw-l3d-cache-refill-wr    |                                          | ⊆ -l3d-cache-refill    | x    |     | x    |     |        |
|                   |      | raw-l3d-cache-wb           | L3 => MEM                                |                        | x    |     | x    |     |        |
|                   |      | raw-l3d-cache-wb-clean     |                                          | ⊆ -l3d-cache-wb        | x    |     | x    |     |        |
|                   |      | raw-l3d-cache-wb-victim    |                                          | ⊆ -l3d-cache-wb        | x    |     | x    |     |        |
|                   |      | raw-l3d-cache-inval        |                                          |                        | x    |     | x    |     |        |
| LL Cache          |      | raw-ll-cache               | = -l3d-cache                             |                        | x    |     | x    |     |        |
|                   |      | raw-ll-cache-miss          | = -l3d-cache-refill                      | ⊆ -ll-cache            | x    |     | x    |     |        |
|                   | 0x36 | raw-ll-cache-rd            | = -l3d-cache-rd                          | ⊆ -ll-cache            |      |     |      |     |        |
|                   | 0x37 | raw-ll-cache-miss-rd       | = -l3d-cache-refill-rd                   | ⊆ -ll-cache-rd         |      |     |      |     |        |
| stall             |      | raw-stall                  | = -frontend ∪ -backend                   |                        | x    |     | x    |     |        |
|                   | 0x23 | raw-stall-frontend         |                                          | ⊆ -stall-frontend      |      |     |      |     |        |
|                   | 0x24 | raw-stall-backend          |                                          | ⊆ -backend-frontend    |      |     |      |     |        |
|                   |      | raw-stall-slot             | = -frontend ∪ -backend                   |                        | x    |     | x    |     | x      |
|                   |      | raw-stall-slot-frontend    |                                          | ⊆ -stall-slot          | x    |     | x    |     | x      |
|                   |      | raw-stall-slot-backend     |                                          | ⊆ -stall-slot          | x    |     | x    |     | x      |
|                   |      | raw-stall-backend-mem      |                                          |                        | x    |     | x    |     |        |
| memory            | 0x13 | raw-mem-access             | = -rd + -wr                              |                        |      |     |      |     |        |
|                   | 0x66 | raw-mem-access-rd          |                                          | ⊆ -mem-access          |      |     |      |     |        |
|                   | 0x67 | raw-mem-access-wr          |                                          | ⊆ -mem-access          |      |     |      |     |        |
|                   | 0x1A | raw-memory-error           |                                          |                        |      |     | x    |     |        |
| remote            | 0x31 | raw-remote-access          |                                          |                        |      |     | x    |     |        |
|                   |      | raw-remote-access-rd       |                                          | ⊆ -remote-access       | x    |     | x    |     |        |
| sample            |      | raw-sample-feed            |                                          |                        | x    |     | x    |     | x      |
|                   |      | raw-sample-filtrate        |                                          |                        | x    |     | x    |     | x      |
|                   |      | raw-sample-pop             |                                          |                        | x    |     | x    |     | x      |
|                   |      | raw-sample-collision       |                                          |                        | x    |     | x    |     | x      |
| other             | 0x1E | raw-chain                  |                                          |                        |      | x   |      |     |        |
