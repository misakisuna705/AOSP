# pmu

<!-- vim-markdown-toc GFM -->

* [Cortex A76](#cortex-a76)

<!-- vim-markdown-toc -->

## Cortex A76

```zsh
simpleperf list raw
```

| type           | number | event                      | description                                                                                | note                      |
| -------------- | ------ | -------------------------- | ------------------------------------------------------------------------------------------ | ------------------------- |
| cycle          |        | raw-cpu-cycles             | Cycle                                                                                      |                           |
|                |        | raw-bus-cycles             | Bus cycle                                                                                  |                           |
|                |        | raw-cnt-cycles             | Constant frequency cycles                                                                  |                           |
| instruction    |        | raw-inst-retired           | Instruction architecturally executed                                                       |                           |
|                |        | raw-br-retired             | Instruction architecturally executed, branch                                               |                           |
|                |        | raw-br-immed-retired       | Instruction architecturally executed, immediate branch                                     |                           |
|                |        | raw-br-mis-pred-retired    | Instruction architecturally executed, mispredicted branch                                  |                           |
|                |        | raw-ld-retired             | Instruction architecturally executed, Condition code check pass, load                      |                           |
|                |        | raw-st-retired             | Instruction architecturally executed, Condition code check pass, store                     |                           |
|                |        | raw-unaligned-ldst-retired | Instruction architecturally executed, Condition code check pass, unaligned load or store   |                           |
|                |        | raw-pc-write-retired       | Instruction architecturally executed, Condition code check pass, software change of the PC |                           |
|                | 0x0    | raw-sw-incr                | Instruction architecturally executed, Condition code check pass, software increment        |                           |
|                |        | raw-ttbr-write-retired     | Instruction architecturally executed, Condition code check pass, write to TTBR             |                           |
|                |        | raw-cid-write-retired      | Instruction architecturally executed, Condition code check pass, write to CONTEXTIDR       |                           |
|                |        | raw-exc-return             | Instruction architecturally executed, Condition code check pass, exception return          |                           |
|                |        | raw-br-return-retired      | Instruction architecturally executed, Condition code check pass, procedure return          |                           |
|                |        | raw-sve-inst-retired       | SVE Instructions architecturally executed                                                  |                           |
|                |        | raw-inst-spec              | Operation Speculatively executed                                                           |                           |
|                |        | raw-ldst-spec              | Operation speculatively executed, load or store                                            |                           |
|                |        | raw-ld-spec                | Operation speculatively executed, load                                                     |                           |
|                |        | raw-st-spec                | Operation speculatively executed, store                                                    |                           |
|                |        | raw-pc-write-spec          | Operation speculatively executed, software change of the PC                                |                           |
|                |        | raw-dp-spec                | Operation speculatively executed, integer data processing                                  |                           |
|                |        | raw-vfp-spec               | Operation speculatively executed, floating-point instruction                               |                           |
|                |        | raw-ase-spec               | Operation speculatively executed, Advanced SIMD instruction                                |                           |
|                |        | raw-crypto-spec            | Operation speculatively executed, Cryptographic instruction                                |                           |
|                |        | raw-br-pred                | Predictable branch Speculatively executed                                                  |                           |
|                |        | raw-br-immed-spec          | Branch speculatively executed, immediate branch                                            |                           |
|                |        | raw-br-indirect-spec       | Branch speculatively executed, indirect branch                                             |                           |
|                |        | raw-br-return-spec         | Branch speculatively executed, procedure return                                            |                           |
|                |        | raw-br-mis-pred            | Mispredicted or not predicted branch Speculatively executed                                |                           |
|                |        | raw-ldrex-spec             | Exclusive operation speculatively executed, LDREX or LDX                                   |                           |
|                |        | raw-strex-fail-spec        | Exclusive operation speculatively executed, STREX or STX fail                              |                           |
|                |        | raw-strex-pass-spec        | Exclusive operation speculatively executed, STREX or STX pass                              |                           |
|                |        | raw-strex-spec             | Exclusive operation speculatively executed, STREX or STX                                   |                           |
|                |        | raw-dmb-spec               | Barrier speculatively executed, DMB                                                        |                           |
|                |        | raw-dsb-spec               | Barrier speculatively executed, DSB                                                        |                           |
|                |        | raw-isb-spec               | Barrier speculatively executed, ISB                                                        |                           |
|                |        | raw-op-retired             | Micro-operation architecturally executed                                                   |                           |
|                |        | raw-op-spec                | Micro-operation Speculatively executed                                                     |                           |
|                |        | raw-rc-ld-spec             | Release consistency operation speculatively executed, Load-Acquire                         |                           |
|                |        | raw-rc-st-spec             | Release consistency operation speculatively executed, Store-Release                        |                           |
|                |        | raw-sve-inst-spec          | SVE Instructions speculatively executed                                                    |                           |
|                |        | raw-bus-access             | Bus access                                                                                 |                           |
|                |        | raw-bus-access-rd          | Bus access, read                                                                           |                           |
|                |        | raw-bus-access-wr          | Bus access, write                                                                          |                           |
|                |        | raw-bus-access-normal      | Bus access, normal                                                                         |                           |
|                |        | raw-bus-access-shared      | Bus access, Normal, Cacheable, Shareable                                                   |                           |
|                |        | raw-bus-access-not-shared  | Bus access, not Normal, Cacheable, Shareable                                               |                           |
|                |        | raw-bus-access-periph      | Bus access, peripheral                                                                     |                           |
|                |        | raw-dtlb-walk              | Attributable data or unified TLB access with at least one translation table walk           |                           |
|                |        | raw-exc-dabort             | Exception taken, Data Abort and SError                                                     |                           |
|                |        | raw-exc-fiq                | Exception taken, FIQ                                                                       |                           |
|                |        | raw-exc-hvc                | Exception taken, Hypervisor Call                                                           |                           |
|                |        | raw-exc-irq                | Exception taken, IRQ                                                                       |                           |
|                |        | raw-exc-pabort             | Exception taken, Instruction Abort                                                         |                           |
|                |        | raw-exc-smc                | Exception taken, Secure Monitor Call                                                       |                           |
|                |        | raw-exc-svc                | Exception taken, Supervisor Call                                                           |                           |
|                |        | raw-exc-taken              | Exception taken                                                                            |                           |
|                |        | raw-exc-trap-dabort        | Exception taken, Data Abort or SError not Taken locallyb                                   |                           |
|                |        | raw-exc-trap-fiq           | Exception taken, FIQ not Taken locallyb                                                    |                           |
|                |        | raw-exc-trap-irq           | Exception taken, IRQ not Taken locallyb                                                    |                           |
|                |        | raw-exc-trap-other         | Exception taken, Other traps not Taken locallyb                                            |                           |
|                |        | raw-exc-trap-pabort        | Exception taken, Instruction Abort not Taken locallyb                                      |                           |
|                |        | raw-exc-undef              | Exception taken, Other synchronous                                                         |                           |
|                |        | raw-itlb-walk              | Attributable instruction TLB access with at least one translation table walk               |                           |
| L1 I-Cache     | 0x14   | raw-l1i-cache              |                                                                                            |                           |
|                | 0x1    | raw-l1i-cache-refill       |                                                                                            | ⊆ raw-l1i-cache           |
|                |        | raw-l1i-cache-lmiss        |                                                                                            | ⊆ raw-l1i-cache-refill    |
| L1 I-Cache TLB | 0x26   | raw-l1i-tlb                |                                                                                            |                           |
|                | 0x2    | raw-l1i-tlb-refill         |                                                                                            | ⊆ raw-l1i-tlb             |
| L1 D-Cache     | 0x4    | raw-l1d-cache              | = -rd + -wr                                                                                |                           |
|                | 0x40   | raw-l1d-cache-rd           | CPU <= L1                                                                                  | ⊆ raw-l1d-cache           |
|                | 0x41   | raw-l1d-cache-wr           | CPU => L1                                                                                  | ⊆ raw-l1d-cache           |
|                |        | raw-l1d-cache-allocate     |                                                                                            | ⊆ raw-l1d-cache-wr        |
|                | 0x3    | raw-l1d-cache-refill       | = -rd + -wr = -inner + -outer                                                              | ⊆ raw-l1d-cache-wr        |
|                | 0x44   | raw-l1d-cache-refill-inner | L1 miss, L2 and L3 hit                                                                     | ⊆ raw-l1d-cache-refill    |
|                | 0x45   | raw-l1d-cache-refill-outer | L1 miss, L2 or L3 miss                                                                     | ⊆ raw-l1d-cache-refill    |
|                | 0x42   | raw-l1d-cache-refill-rd    |                                                                                            | ⊆ raw-l1d-cache-refill    |
|                |        | raw-l1d-cache-lmiss-rd     |                                                                                            | ⊆ raw-l1d-cache-refill-rd |
|                | 0x43   | raw-l1d-cache-refill-wr    |                                                                                            | ⊆ raw-l1d-cache-refill    |
|                | 0x15   | raw-l1d-cache-wb           | L1 => L2                                                                                   |                           |
|                | 0x46   | raw-l1d-cache-wb-victim    |                                                                                            | ⊆ raw-l1d-cache-wb        |
|                | 0x47   | raw-l1d-cache-wb-clean     |                                                                                            | ⊆ raw-l1d-cache-wb        |
|                | 0x48   | raw-l1d-cache-inval        |                                                                                            |                           |
| L1 D-Cache TLB | 0x25   | raw-l1d-tlb                | = -rd + -wr                                                                                |                           |
|                | 0x4E   | raw-l1d-tlb-rd             |                                                                                            | ⊆ raw-l1d-tlb             |
|                | 0x4F   | raw-l1d-tlb-wr             |                                                                                            | ⊆ raw-l1d-tlb             |
|                | 0x5    | raw-l1d-tlb-refill         | = -rd + -wr                                                                                | ⊆ raw-l1d-tlb-wr          |
|                | 0x4C   | raw-l1d-tlb-refill-rd      |                                                                                            | ⊆ raw-l1d-tlb-refill      |
|                | 0x4D   | raw-l1d-tlb-refill-wr      |                                                                                            | ⊆ raw-l1d-tlb-refill      |
| L2 I-Cache     |        | raw-l2i-cache              |                                                                                            |                           |
|                |        | raw-l2i-cache-refill       |                                                                                            | ⊆ raw-l2i-cache           |
|                |        | raw-l2i-cache-lmiss        |                                                                                            | ⊆ raw-l2i-cache-refill    |
| L2 I-Cache TLB |        | raw-l2i-tlb                |                                                                                            |                           |
|                |        | raw-l2i-tlb-refill         |                                                                                            | ⊆ raw-l2i-tlb             |
| L2 D-Cache     | 0x16   | raw-l2d-cache              | = -rd + -wr                                                                                |                           |
|                | 0x50   | raw-l2d-cache-rd           | L1 <= L2                                                                                   | ⊆ raw-l2d-cache           |
|                | 0x51   | raw-l2d-cache-wr           | ≈ raw-l1d-cache-wb (L1 => L2)                                                              | ⊆ raw-l2d-cache           |
|                | 0x20   | raw-l2d-cache-allocate     | ≈ raw-l2d-cache-wr                                                                         | ⊆ raw-l2d-cache-wr        |
|                | 0x17   | raw-l2d-cache-refill       | = -rd + -wr                                                                                | ⊆ raw-l2d-cache-wr        |
|                | 0x52   | raw-l2d-cache-refill-rd    |                                                                                            | ⊆ raw-l2d-cache-refill    |
|                |        | raw-l2d-cache-lmiss-rd     |                                                                                            | ⊆ raw-l2d-cache-refill-rd |
|                | 0x53   | raw-l2d-cache-refill-wr    |                                                                                            | ⊆ raw-l2d-cache-refill    |
|                | 0x18   | raw-l2d-cache-wb           | L2 => L3                                                                                   |                           |
|                | 0x56   | raw-l2d-cache-wb-victim    |                                                                                            | ⊆ raw-l2d-cache-wb        |
|                | 0x57   | raw-l2d-cache-wb-clean     |                                                                                            | ⊆ raw-l2d-cache-wb        |
|                | 0x58   | raw-l2d-cache-inval        |                                                                                            |                           |
| L2 D-Cache TLB | 0x2F   | raw-l2d-tlb                | = -rd + -wr                                                                                |                           |
|                | 0x5E   | raw-l2d-tlb-rd             |                                                                                            | ⊆ raw-l2d-tlb             |
|                | 0x5F   | raw-l2d-tlb-wr             |                                                                                            | ⊆ raw-l2d-tlb             |
|                | 0x2D   | raw-l2d-tlb-refill         | = -rd + -wr                                                                                | ⊆ raw-l2d-tlb-wr          |
|                | 0x5C   | raw-l2d-tlb-refill-rd      |                                                                                            | ⊆ raw-l2d-tlb-refill      |
|                | 0x5D   | raw-l2d-tlb-refill-wr      |                                                                                            | ⊆ raw-l2d-tlb-refill      |
| L3 D-Cache     | 0x2B   | raw-l3d-cache              | = -rd + -wr                                                                                |                           |
|                |        | raw-l3d-cache-rd           |                                                                                            | ⊆ raw-l3d-cache           |
|                |        | raw-l3d-cache-wr           | ≈ raw-l2d-cache-wb (L2 => L3)                                                              | ⊆ raw-l3d-cache           |
|                | 0x29   | raw-l3d-cache-allocate     | ≈ raw-l3d-cache-wr                                                                         | ⊆ raw-l3d-cache-wr        |
|                | 0x2A   | raw-l3d-cache-refill       | = -rd + -wr                                                                                | ⊆ raw-l3d-cache-wr        |
|                |        | raw-l3d-cache-refill-rd    |                                                                                            | ⊆ raw-l3d-cache-refill    |
|                |        | raw-l3d-cache-lmiss-rd     |                                                                                            | ⊆ raw-l3d-cache-refill-rd |
|                |        | raw-l3d-cache-refill-wr    |                                                                                            | ⊆ raw-l3d-cache-refill    |
|                |        | raw-l3d-cache-wb           | L3 => MEM                                                                                  |                           |
|                |        | raw-l3d-cache-wb-clean     |                                                                                            | ⊆ raw-l3d-cache-wb        |
|                |        | raw-l3d-cache-wb-victim    |                                                                                            | ⊆ raw-l3d-cache-wb        |
|                |        | raw-l3d-cache-inval        |                                                                                            |                           |
| LL Cache       |        | raw-ll-cache               | = raw-l3d-cache                                                                            |                           |
|                |        | raw-ll-cache-miss          | = raw-l3d-cache-refill                                                                     | ⊆ raw-ll-cache            |
|                | 0x36   | raw-ll-cache-rd            | = raw-l3d-cache-rd                                                                         | ⊆ raw-ll-cache            |
|                | 0x37   | raw-ll-cache-miss-rd       | = raw-l3d-cache-refill-rd                                                                  | ⊆ raw-ll-cache-rd         |
| stall          |        | raw-stall                  | No operation sent for execution                                                            |                           |
|                |        | raw-stall-backend          | No operation issued due to backend                                                         |                           |
|                |        | raw-stall-backend-mem      | Memory stall cycles                                                                        |                           |
|                |        | raw-stall-frontend         | No operation issued due to the frontend                                                    |                           |
|                |        | raw-stall-slot             | No operation sent for execution on a Slot                                                  |                           |
|                |        | raw-stall-slot-backend     | No operation sent for execution on a Slot due to the backend                               |                           |
|                |        | raw-stall-slot-frontend    | No operation send for execution on a Slot due to the frontend                              |                           |
| memory         |        | raw-mem-access             | Data memory access                                                                         |                           |
|                |        | raw-mem-access-rd          | Data memory access, read                                                                   |                           |
|                |        | raw-mem-access-wr          | Data memory access, write                                                                  |                           |
|                |        | raw-memory-error           | Local memory error                                                                         |                           |
| remote         |        | raw-remote-access          | Attributable access to another socket in a multi-socket system                             |                           |
|                |        | raw-remote-access-rd       | Attributable memory read access to another socket in a multi-socket system                 |                           |
| unaligned      |        | raw-unaligned-ldst-spec    | Unaligned access                                                                           |                           |
|                |        | raw-unaligned-ld-spec      | Unaligned access, read                                                                     |                           |
|                |        | raw-unaligned-st-spec      | Unaligned access, write                                                                    |                           |
| sample         |        | raw-sample-feed            | Sample Taken                                                                               |                           |
|                |        | raw-sample-filtrate        | Sample Taken and not removed by filtering                                                  |                           |
|                |        | raw-sample-pop             | Sample Population                                                                          |                           |
|                |        | raw-sample-collision       | Sample collided with previous sample                                                       |                           |
|                | 0x1E   | raw-chain                  |                                                                                            |                           |
