# pmu

<!-- vim-markdown-toc GFM -->

* [Cortex A76](#cortex-a76)

<!-- vim-markdown-toc -->

## Cortex A76

```zsh
simpleperf list raw
```

| type              | id   | event                      | description                      | note                      | spec |
| ----------------- | ---- | -------------------------- | -------------------------------- | ------------------------- | ---- |
| cycle             | 0x11 | raw-cpu-cycles             |                                  |                           |      |
|                   | 0x1D | raw-bus-cycles             | = -cpu-cycles                    |                           |      |
|                   |      | raw-cnt-cycles             |                                  |                           |      |
| instr.            | 0x8  | raw-inst-retired           |                                  |                           |      |
| instr. branch     | 0x21 | raw-br-retired             |                                  | ⊆ raw-inst-retired        |      |
|                   |      | raw-br-immed-retired       |                                  | ⊆ raw-br-retired          |      |
|                   |      | raw-br-return-retired      |                                  | ⊆ raw-br-retired          |      |
|                   | 0x22 | raw-br-mis-pred-retired    |                                  | ⊆ raw-br-retired          |      |
| instr. load/store |      | raw-ld-retired             |                                  | ⊆ raw-inst-retired        |      |
|                   |      | raw-st-retired             |                                  | ⊆ raw-inst-retired        |      |
|                   |      | raw-unaligned-ldst-retired |                                  | ⊆ raw-inst-retired        |      |
| instr. other      |      | raw-op-retired             |                                  | ⊆ raw-inst-retired        |      |
|                   |      | raw-sve-inst-retired       |                                  | ⊆ raw-inst-retired        |      |
|                   |      | raw-pc-write-retired       |                                  | ⊆ raw-inst-retired        |      |
| 0x1C              |      | raw-ttbr-write-retired     |                                  | ⊆ raw-inst-retired        |      |
|                   | 0x0B | raw-cid-write-retired      |                                  | ⊆ raw-inst-retired        |      |
|                   | 0x0A | raw-exc-return             |                                  | ⊆ raw-inst-retired        |      |
|                   | 0x0  | raw-sw-incr                |                                  | ⊆ raw-inst-retired        |      |
| op.               | 0x1B | raw-inst-spec              | ≈ -retired                       |                           |      |
| op. branch        | 0x12 | raw-br-pred                | ≈ -retired                       | ⊆ raw-inst-spec           |      |
|                   | 0x78 | raw-br-immed-spec          | ≈ -retired                       | ⊆ raw-br-pred             |      |
|                   | 0x79 | raw-br-return-spec         | ≈ -retired                       | ⊆ raw-br-pred             |      |
|                   | 0x7A | raw-br-indirect-spec       |                                  | ⊆ raw-br-pred             |      |
|                   | 0x10 | raw-br-mis-pred            | ≈ -retired                       | ⊆ raw-br-pred             |      |
| op. load/store    | 0x72 | raw-ldst-spec              | ≈ -retired = -ld-spec + -st-spec | ⊆ raw-inst-spec           |      |
|                   | 0x70 | raw-ld-spec                | ≈ -retired                       | ⊆ raw-ldst-spec           |      |
|                   | 0x71 | raw-st-spec                | ≈ -retired                       | ⊆ raw-ldst-spec           |      |
|                   | 0x6A | raw-unaligned-ldst-spec    | = -ld-spec + -st-spec            | ⊆ raw-inst-spec           |      |
|                   | 0x68 | raw-unaligned-ld-spec      |                                  | ⊆ raw-unaligned-ldst-spec |      |
|                   | 0x69 | raw-unaligned-st-spec      |                                  | ⊆ raw-unaligned-ldst-spec |      |
| op. other         |      | raw-op-spec                | ≈ -retired                       | ⊆ raw-inst-spec           |      |
|                   |      | raw-sve-inst-spec          | ≈ -retired                       | ⊆ raw-inst-spec           |      |
|                   | 0x76 | raw-pc-write-spec          | ≈ -retired                       | ⊆ raw-inst-spec           |      |
|                   | 0x74 | raw-ase-spec               |                                  | ⊆ raw-inst-spec           |      |
|                   | 0x77 | raw-crypto-spec            |                                  | ⊆ raw-inst-spec           |      |
|                   | 0x73 | raw-dp-spec                |                                  | ⊆ raw-inst-spec           |      |
|                   | 0x75 | raw-vfp-spec               |                                  | ⊆ raw-inst-spec           |      |
|                   | 0x6C | raw-ldrex-spec             |                                  | ⊆ raw-inst-spec           |      |
|                   | 0x6F | raw-strex-spec             | = -pass-spec + -fail-spec        | ⊆ raw-inst-spec           |      |
|                   | 0x6D | raw-strex-pass-spec        |                                  | ⊆ raw-strex-spec          |      |
|                   | 0x6E | raw-strex-fail-spec        |                                  | ⊆ raw-strex-spec          |      |
|                   | 0x90 | raw-rc-ld-spec             |                                  | ⊆ raw-inst-spec           |      |
|                   | 0x91 | raw-rc-st-spec             |                                  | ⊆ raw-inst-spec           |      |
|                   | 0x7C | raw-isb-spec               |                                  | ⊆ raw-inst-spec           |      |
|                   | 0x7D | raw-dsb-spec               |                                  | ⊆ raw-inst-spec           |      |
|                   | 0x7E | raw-dmb-spec               |                                  | ⊆ raw-inst-spec           |      |
| bus               | 0x19 | raw-bus-access             | -rd + -wr                        |                           |      |
|                   | 0x60 | raw-bus-access-rd          |                                  | ⊆ raw-bus-access          |      |
|                   | 0x61 | raw-bus-access-wr          |                                  | ⊆ raw-bus-access          |      |
|                   |      | raw-bus-access-normal      |                                  | ⊆ raw-bus-access          |      |
|                   |      | raw-bus-access-shared      |                                  | ⊆ raw-bus-access          |      |
|                   |      | raw-bus-access-not-shared  |                                  | ⊆ raw-bus-access          |      |
|                   |      | raw-bus-access-periph      |                                  | ⊆ raw-bus-access          |      |
| exception         | 0x9  | raw-exc-taken              |                                  |                           |      |
|                   | 0x81 | raw-exc-undef              |                                  | ⊆ raw-exc-taken           |      |
|                   | 0x82 | raw-exc-svc                |                                  | ⊆ raw-exc-taken           |      |
|                   | 0x83 | raw-exc-pabort             |                                  | ⊆ raw-exc-taken           |      |
|                   | 0x8B | raw-exc-trap-pabort        |                                  | ⊆ raw-exc-pabort          |      |
|                   | 0x84 | raw-exc-dabort             |                                  | ⊆ raw-exc-taken           |      |
|                   | 0x8C | raw-exc-trap-dabort        |                                  | ⊆ raw-exc-dabort          |      |
|                   | 0x86 | raw-exc-irq                |                                  | ⊆ raw-exc-taken           |      |
|                   | 0x8E | raw-exc-trap-irq           |                                  | ⊆ raw-exc-irq             |      |
|                   | 0x87 | raw-exc-fiq                |                                  | ⊆ raw-exc-taken           |      |
|                   | 0x8F | raw-exc-trap-fiq           |                                  | ⊆ raw-exc-fiq             |      |
|                   | 0x88 | raw-exc-smc                |                                  | ⊆ raw-exc-taken           |      |
|                   | 0x8A | raw-exc-hvc                |                                  | ⊆ raw-exc-taken           |      |
|                   | 0x8D | raw-exc-trap-other         |                                  | ⊆ raw-exc-taken           |      |
| L1 I-Cache        | 0x14 | raw-l1i-cache              |                                  |                           |      |
|                   | 0x1  | raw-l1i-cache-refill       |                                  | ⊆ raw-l1i-cache           |      |
|                   |      | raw-l1i-cache-lmiss        |                                  | ⊆ raw-l1i-cache-refill    |      |
| L1 I-Cache TLB    | 0x26 | raw-l1i-tlb                |                                  |                           |      |
|                   | 0x2  | raw-l1i-tlb-refill         |                                  | ⊆ raw-l1i-tlb             |      |
| L1 D-Cache        | 0x4  | raw-l1d-cache              | = -rd + -wr                      |                           |      |
|                   | 0x40 | raw-l1d-cache-rd           | CPU <= L1                        | ⊆ raw-l1d-cache           |      |
|                   | 0x41 | raw-l1d-cache-wr           | CPU => L1                        | ⊆ raw-l1d-cache           |      |
|                   |      | raw-l1d-cache-allocate     |                                  | ⊆ raw-l1d-cache-wr        |      |
|                   | 0x3  | raw-l1d-cache-refill       | = -rd + -wr = -inner + -outer    | ⊆ raw-l1d-cache-wr        |      |
|                   | 0x44 | raw-l1d-cache-refill-inner | L1 miss, L2 and L3 hit           | ⊆ raw-l1d-cache-refill    |      |
|                   | 0x45 | raw-l1d-cache-refill-outer | L1 miss, L2 or L3 miss           | ⊆ raw-l1d-cache-refill    |      |
|                   | 0x42 | raw-l1d-cache-refill-rd    |                                  | ⊆ raw-l1d-cache-refill    |      |
|                   |      | raw-l1d-cache-lmiss-rd     |                                  | ⊆ raw-l1d-cache-refill-rd |      |
|                   | 0x43 | raw-l1d-cache-refill-wr    |                                  | ⊆ raw-l1d-cache-refill    |      |
|                   | 0x15 | raw-l1d-cache-wb           | L1 => L2                         |                           |      |
|                   | 0x46 | raw-l1d-cache-wb-victim    |                                  | ⊆ raw-l1d-cache-wb        |      |
|                   | 0x47 | raw-l1d-cache-wb-clean     |                                  | ⊆ raw-l1d-cache-wb        |      |
|                   | 0x48 | raw-l1d-cache-inval        |                                  |                           |      |
| L1 D-Cache TLB    | 0x25 | raw-l1d-tlb                | = -rd + -wr                      |                           |      |
|                   | 0x4E | raw-l1d-tlb-rd             |                                  | ⊆ raw-l1d-tlb             |      |
|                   | 0x4F | raw-l1d-tlb-wr             |                                  | ⊆ raw-l1d-tlb             |      |
|                   | 0x5  | raw-l1d-tlb-refill         | = -rd + -wr                      | ⊆ raw-l1d-tlb-wr          |      |
|                   | 0x4C | raw-l1d-tlb-refill-rd      |                                  | ⊆ raw-l1d-tlb-refill      |      |
|                   | 0x4D | raw-l1d-tlb-refill-wr      |                                  | ⊆ raw-l1d-tlb-refill      |      |
| L2 I-Cache        |      | raw-l2i-cache              |                                  |                           |      |
|                   |      | raw-l2i-cache-refill       |                                  | ⊆ raw-l2i-cache           |      |
|                   |      | raw-l2i-cache-lmiss        |                                  | ⊆ raw-l2i-cache-refill    |      |
| L2 I-Cache TLB    |      | raw-l2i-tlb                |                                  |                           |      |
|                   |      | raw-l2i-tlb-refill         |                                  | ⊆ raw-l2i-tlb             |      |
| L2 D-Cache        | 0x16 | raw-l2d-cache              | = -rd + -wr                      |                           |      |
|                   | 0x50 | raw-l2d-cache-rd           | L1 <= L2                         | ⊆ raw-l2d-cache           |      |
|                   | 0x51 | raw-l2d-cache-wr           | ≈ -l1d-cache-wb (L1 => L2)       | ⊆ raw-l2d-cache           |      |
|                   | 0x20 | raw-l2d-cache-allocate     | ≈ -l2d-cache-wr                  | ⊆ raw-l2d-cache-wr        |      |
|                   | 0x17 | raw-l2d-cache-refill       | = -rd + -wr                      | ⊆ raw-l2d-cache-wr        |      |
|                   | 0x52 | raw-l2d-cache-refill-rd    |                                  | ⊆ raw-l2d-cache-refill    |      |
|                   |      | raw-l2d-cache-lmiss-rd     |                                  | ⊆ raw-l2d-cache-refill-rd |      |
|                   | 0x53 | raw-l2d-cache-refill-wr    |                                  | ⊆ raw-l2d-cache-refill    |      |
|                   | 0x18 | raw-l2d-cache-wb           | L2 => L3                         |                           |      |
|                   | 0x56 | raw-l2d-cache-wb-victim    |                                  | ⊆ raw-l2d-cache-wb        |      |
|                   | 0x57 | raw-l2d-cache-wb-clean     |                                  | ⊆ raw-l2d-cache-wb        |      |
|                   | 0x58 | raw-l2d-cache-inval        |                                  |                           |      |
| L2 D-Cache TLB    | 0x2F | raw-l2d-tlb                | = -rd + -wr                      |                           |      |
|                   | 0x5E | raw-l2d-tlb-rd             |                                  | ⊆ raw-l2d-tlb             |      |
|                   | 0x5F | raw-l2d-tlb-wr             |                                  | ⊆ raw-l2d-tlb             |      |
|                   | 0x2D | raw-l2d-tlb-refill         | = -rd + -wr                      | ⊆ raw-l2d-tlb-wr          |      |
|                   | 0x34 | raw-dtlb-walk              | = -l2d-tlb-refill                |                           |      |
|                   | 0x35 | raw-itlb-walk              |                                  |                           |      |
|                   | 0x5C | raw-l2d-tlb-refill-rd      |                                  | ⊆ raw-l2d-tlb-refill      |      |
|                   | 0x5D | raw-l2d-tlb-refill-wr      |                                  | ⊆ raw-l2d-tlb-refill      |      |
| L3 D-Cache        | 0x2B | raw-l3d-cache              | = -rd + -wr                      |                           |      |
|                   |      | raw-l3d-cache-rd           |                                  | ⊆ raw-l3d-cache           |      |
|                   |      | raw-l3d-cache-wr           | ≈ -l2d-cache-wb (L2 => L3)       | ⊆ raw-l3d-cache           |      |
|                   | 0x29 | raw-l3d-cache-allocate     | ≈ -l3d-cache-wr                  | ⊆ raw-l3d-cache-wr        |      |
|                   | 0x2A | raw-l3d-cache-refill       | = -rd + -wr                      | ⊆ raw-l3d-cache-wr        |      |
|                   |      | raw-l3d-cache-refill-rd    |                                  | ⊆ raw-l3d-cache-refill    |      |
|                   |      | raw-l3d-cache-lmiss-rd     |                                  | ⊆ raw-l3d-cache-refill-rd |      |
|                   |      | raw-l3d-cache-refill-wr    |                                  | ⊆ raw-l3d-cache-refill    |      |
|                   |      | raw-l3d-cache-wb           | L3 => MEM                        |                           |      |
|                   |      | raw-l3d-cache-wb-clean     |                                  | ⊆ raw-l3d-cache-wb        |      |
|                   |      | raw-l3d-cache-wb-victim    |                                  | ⊆ raw-l3d-cache-wb        |      |
|                   |      | raw-l3d-cache-inval        |                                  |                           |      |
| LL Cache          |      | raw-ll-cache               | = -l3d-cache                     |                           |      |
|                   |      | raw-ll-cache-miss          | = -l3d-cache-refill              | ⊆ raw-ll-cache            |      |
|                   | 0x36 | raw-ll-cache-rd            | = -l3d-cache-rd                  | ⊆ raw-ll-cache            |      |
|                   | 0x37 | raw-ll-cache-miss-rd       | = -l3d-cache-refill-rd           | ⊆ raw-ll-cache-rd         |      |
| stall             |      | raw-stall                  | = -frontend ∪ -backend           |                           |      |
|                   | 0x23 | raw-stall-frontend         |                                  | ⊆ raw-stall-frontend      |      |
|                   | 0x24 | raw-stall-backend          |                                  | ⊆ raw-backend-frontend    |      |
|                   |      | raw-stall-slot             | = -frontend ∪ -backend           |                           |      |
|                   |      | raw-stall-slot-frontend    |                                  | ⊆ raw-stall-slot          |      |
|                   |      | raw-stall-slot-backend     |                                  | ⊆ raw-stall-slot          |      |
|                   |      | raw-stall-backend-mem      |                                  |                           |      |
| memory            | 0x13 | raw-mem-access             | = -rd + -wr                      |                           |      |
|                   | 0x66 | raw-mem-access-rd          |                                  | ⊆ raw-mem-access          |      |
|                   | 0x67 | raw-mem-access-wr          |                                  | ⊆ raw-mem-access          |      |
|                   | 0x1A | raw-memory-error           |                                  |                           |      |
| remote            | 0x31 | raw-remote-access          |                                  |                           |      |
|                   |      | raw-remote-access-rd       |                                  | ⊆ raw-remote-access       |      |
| sample            |      | raw-sample-feed            |                                  |                           |      |
|                   |      | raw-sample-filtrate        |                                  |                           |      |
|                   |      | raw-sample-pop             |                                  |                           |      |
|                   |      | raw-sample-collision       |                                  |                           |      |
| other             | 0x1E | raw-chain                  |                                  |                           |      |
