---
id: minimal-siegel-compactification-exists
title: A theta compactification of the Siegel moduli scheme (statement form)
kind: theorem
decl: GlobalTheory.T.minimalSiegelCompactification_exists
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MinimalSiegelCompactificationExistsStatement
covers: 361
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It proves the statement $\mathrm{MinSt5}$ by [`minSt5`](/entry/min-st5/), which has the real content. Its one user is [the toroidal compactification](/entry/siegel-toroidal-pol-charts/), where it gives the $Z$ that [`poinSt`](/entry/poin-st/) blows up.

## Statement

Let $\Lambda_n = \mathbb{Z}[\zeta_n, 1/n]$, and let theta compactifications be as in [`poinSt`](/entry/poin-st/).

**Theorem** ($\mathrm{MinSt5}$). For $g \geq 1$, odd $n \geq 3$ and each Siegel family over $\Lambda_n$ with base $X$ and universal abelian scheme $A$, there are $z \colon Z \to \operatorname{Spec} \Lambda_n$, $i \colon X \to Z$ and a line bundle $\mathcal{O}_Z(1)$ with `MinAt5`:

1. $(Z, i)$ is a theta compactification, and $\mathcal{O}_Z(1)$ is an ample line bundle;
2. there are a ring $o'$ with a finite injective map $\beta \colon \Lambda_n \to o'$, a normal scheme $S'$ projective over $o'$, a dense open $U \subset S'$, a finite surjective map $c \colon U \to X$, and a map $\pi \colon S' \to Z$ over $\beta$ with $\pi|_U = i \circ c$. The map $\pi$ is proper and surjective, and $Z$ is noetherian;
3. there is a semi-abelian scheme $G$ over $S'$, smooth of relative dimension $g$, whose restriction to $U$ is $c^*A$;
4. there is $N \geq 1$ with $\pi^*\mathcal{O}_Z(1) \cong \omega_G^{N}$, where $\omega_G$ is the Hodge line bundle `hodge G g`, the determinant of the rank $g$ bundle `LieVB.omega G`.

## Proof

The proof applies `GlobalTheory.SiegMinTop.minSt5`.

## In the Lean code

The theorem is in [MinimalSiegelCompactificationExistsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MinimalSiegelCompactificationExistsStatement.lean#L11). The proof is `first | exact @GlobalTheory.SiegMinTop.minSt5 | ...`, a tactic that tries the alias in three forms. `MinSt5` and `MinAt5` are in [MinSt5OfMinSt4.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/MinSt5OfMinSt4.lean#L36). Clause 1 of `MinAt5` repeats four facts that `IsThetaCompact` already contains (projective, normal, over $\Lambda_n$, dense image). The name says "minimal", but nothing in `MinAt5` asks that $Z$ be minimal.
