---
id: kudla-splitting-split-unitary
title: The Weil representation of a split unitary group, split by a character
kind: theorem
decl: GlobalTheory.kudlaSplittingSplitUnitary
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KudlaSplittingSplitUnitary
covers: 1018
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `KudlaSplittingSplitUnitary`: a linear Weil representation of a split unitary group $U(n,n)$ over a $p$-adic field, with the Levi subgroup acting through a splitting character. Its one user is [the Weil representation of a split unitary group from the literature](/entry/kudla-splitting-split-unitary-of-literature/), which passes it on unchanged. The construction of the representation is done in the lemma `exists_isKW`; this theorem reads off four properties from it.

## Statement

Let $F$ be a non-archimedean local field of characteristic $0$ and $E/F$ a quadratic extension, given by an $F$-automorphism $c$ of $E$ and a unit $\delta$ with $c(\delta) = -\delta$ such that $1, \delta$ is a basis. Let $Q$ be an invertible $m \times m$ matrix over $E$ with $c(Q_{ji}) = Q_{ij}$. Let $\psi$ be a nontrivial continuous unitary character of $F$. Let $\chi$ be a continuous unitary character of $E^\times$ with $\chi(a) = 1$ for $a \in N(E^\times)$ and $\chi(a) = (-1)^m$ for the other $a \in F^\times$. Let $J$ be the standard $2n \times 2n$ form `stdJ`, $G = \{g \in \mathrm{GL}_{2n}(E) : g^{\mathsf T} J\, c(g) = J\}$, and $S$ the space of locally constant functions of compact support on $X = M_{m \times n}(E)$.

**Theorem.** There is a representation $\omega$ of $G$ on $S$ such that:

1. $\omega$ is smooth;
2. each $\omega(g)$ preserves the $L^2$ norm, for every Haar measure on $X$;
3. $H(w)\,\omega(g) = \omega(g)\,H(wg)$ for each $w \in M_{m \times 2n}(E)$, where $H(w)$ is the Heisenberg operator `Heisenberg₂` built from $\psi$ and $Q$;
4. for $a \in \mathrm{GL}_n(E)$ and the Levi element $m(a) = \operatorname{diag}(a, c(a)^{-\mathsf T})$, $(\omega(m(a))\varphi)(x) = \chi(\det a)\,\lvert N_{E/F}(\det a)\rvert_F^{m/2}\,\varphi(xa)$.

The volume 8 entry gives $H(w)$ in full. By its shape, this is the Schrödinger model of the [[Weil representation|H3Q2703KKV]] of $U(n,n)$, made linear by a splitting character in the sense of Kudla (Israel J. Math. 87, 1994).

## Proof

1. `quadExt_topological_properties` gives the topological facts on $X$ that the measure theory needs (fields `grp`, `t2`, `lc` and `sc` of the structure `Good`, which we have not unfolded). Put the Borel structure on $X$.
2. `exists_weil_representation_split_unitary_schwartzBruhat`, for an additive Haar measure $\mu$, gives $\kappa \in \mathbb{C}$ and $\omega$ with `IsKW`. This structure has two fields. On the Siegel parabolic $P$ (the $g$ with lower left block $0$), $\omega(p)\varphi = $ `parFun` $(p)\varphi$, where $(\mathrm{parFun}(g)\varphi)(x) = \mathrm{sc}(\det A)\,\psi\bigl(\tfrac12 \mathrm{pr}(xA, xB)\bigr)\varphi(xA)$ for the upper blocks $A, B$ of $g$. On the Weyl element, $\omega$ is $\kappa$ times a Fourier transform.
3. Properties 1, 2 and 3 follow from `IsKW` by `splitUnitaryWeilRepresentation_isSmooth`, `weil_representation_preserves_L2_space` and `weilRepresentation_intertwines_heisenberg`.
4. For property 4: $m(a)$ lies in $P$, with $A = a$ and $B = 0$. Since $\mathrm{pr}(y, 0) = 0$, the $\psi$ factor is $1$. `unitaryCharacterAbsScalar_basic_properties` gives $\mathrm{sc}(z) = \chi(z)\lvert N(z)\rvert_F^{m/2}$ for $z \in E^\times$. The rest is bookkeeping.

## In the Lean code

The theorem is at [KudlaSplittingSplitUnitary.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KudlaSplittingSplitUnitary.lean#L17). The statement is at [KudlaSplittingSplitUnitary.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/KudlaSplittingSplitUnitary.lean#L223). `IsKW`, `parFun` and `sc` are in [UnipVal.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/UnipVal.lean#L134).

- The five lemmas from `GlobalTheory.T` are one-line wrappers of `KSp.Exist.exists_isKW`, `KSp.isKW_isSmoothRep`, `KSp.weil_representation_preserves_L2`, `KSp.weil_heis_intertwine` and `KSp.sc_basic`. Most of the 1,018 declarations below this theorem are under `exists_isKW`, which builds $\omega$ from the action of $P$ and the Weyl element.
- The conclusion forgets the Weyl element formula and the constant $\kappa$ of `IsKW`. It does not say that $\omega$ is unique.
