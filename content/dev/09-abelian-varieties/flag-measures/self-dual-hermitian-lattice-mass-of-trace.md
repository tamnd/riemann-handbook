---
id: self-dual-hermitian-lattice-mass-of-trace
title: The mass of self-dual lattices over a frame lattice, statement form
kind: theorem
decl: GlobalTheory.T.selfDualHermitianLattice_mass_of_trace
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.SelfDualHermitianLatticeMassOfTraceStatement
covers: 333
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`mass_trace`](/entry/mass-trace/). It has two users, `GenMass.total_le_generic` and `DefectShare.share_le`, both in this volume. So in the dominator tree it hangs directly below the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/). The content is in [`mass_trace`](/entry/mass-trace/).

## Statement

**Theorem.** Let $S$ be a frames record with $k \ge 2r + 6$ whose Hermitian form has a self-dual lattice. There is $\kappa > 0$ such that for each frame class $C$, each pair $p \in C$ and each lattice $\hat M$ with $M(p) \subseteq \hat M \subseteq \mathrm{ME}$ on which $h$ is integral,

$$\tfrac{\kappa}{2}\, [\hat M : M(p)]^{-(k-1)} \le \sigma(\hat M) \le 2\kappa\, [\hat M : M(p)]^{-(k-1)}.$$

Here $\sigma(\hat M)$ is the weighted number of self-dual lattices $\Lambda$ with $\Lambda \cap \mathrm{ME} = \hat M$ (`massSig`), and $M(p)$ is the lattice spanned by the frame pair $p$. All objects are defined in [the entry for `mass_trace`](/entry/mass-trace/).

## Proof

The proof is the term `GlobalTheory.HL.FrameMass.mass_trace`. There is nothing else.

## In the Lean code

The theorem is at [SelfDualHermitianLatticeMassOfTraceStatement.lean line 9](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/SelfDualHermitianLatticeMassOfTraceStatement.lean#L9). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The two statements are the same, so the first alternative fits. Both users call it with $k \ge 4r + 7$.
