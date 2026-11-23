---
id: all-thm-t
title: ThmT for every non-archimedean local field
kind: theorem
decl: PositivityTheory.RgUd.All.thmT
module: Development.WeilBound.RepresentationTheoryGL.UnitaryDualProof.BernsteinExponentBounds.BernAll
covers: 686
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{ThmT}(k)$ for every non-archimedean local field $k$. It only splits on the characteristic of $k$ and passes to the two cases: [the case of characteristic $p$](/entry/tp-final-thm-t/) and [the case of characteristic zero](/entry/t-final-thm-t/). Those two entries have the real content. Its only caller is [ThmB](/entry/thm-b/).

## Statement

We use $X_n$, $B_Z$, $G_Z$ and $\mathrm{Van}(Z)$ as in [the characteristic zero entry](/entry/t-final-thm-t/).

**Theorem** ($\mathrm{ThmT}(k)$). For each $n$ and each commutative reduced subalgebra $Z \subseteq M_n(k)$, $\mathrm{Van}(Z)$ holds: a $G_Z$-invariant distribution on $X_n$ supported on $B_Z \times k^n$ vanishes on functions supported in $\{v \neq 0\}$.

## Proof

Let $p$ be the characteristic of $k$ (`CharP.exists`). By `CharP.char_is_prime_or_zero`, $p$ is prime or $p = 0$. If $p$ is prime, apply `TP.Final.thmT k p`. If $p = 0$, then $k$ has characteristic zero, and we apply `T.Final.thmT k`. There is nothing else.

## In the Lean code

The theorem is at [BernAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/BernAll.lean#L13). `ThmT` is in [IsInvForm.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/IsInvForm.lean#L54). The two cases use different methods: an induction on the dimension of $B_Z$ in characteristic zero, and an induction on the measure $\mu$ from a descent statement in characteristic $p$. Only the characteristic $p$ case is counted in the size of this declaration. The characteristic zero case is also used by `thmB_char0` in ThmBChar0.lean, so it is not dominated by this theorem.
