---
id: u-poin-st-x-sep
title: The normalized blowup of the compactification, with separation
kind: theorem
decl: GlobalTheory.UPoincTop.uPoinStX_sep
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnitaryToroidalSeparationOfBase
covers: 1389
status: drafted
drafted_by: writer@claude
---
This theorem starts from a projective normal compactification $Z$ of a unitary moduli scheme over the coefficient field. It blows up $Z$ along a boundary ideal that a fan function $\varphi$ gives, and it proves the separation property `SepB` for the normalized blowup $S$. The result goes to [rigid boundary charts for a fan](/entry/rigid-for-fan-holds/) under the names [`uStB`](/entry/u-st-b/) and [`unitaryToroidalSeparation_of_base`](/entry/unitary-toroidal-separation-of-base/). Below this theorem are 1,389 declarations of the proof.

## Statement

Take $E$, $H$, a datum of signature $(p, q)$ with $p + q \geq 1$, $\varphi$ with `IsPolFan` and `NoSelfInt`, the moduli scheme $X$ and the field $F$, as in [rigid boundary charts for a fan](/entry/rigid-for-fan-holds/).

**Theorem.** There are $i \colon X_F \to Z$, $\pi \colon S \to Z$, $j \colon X_F \to S$, a line bundle $\mathcal{O}_Z(1)$, integers $N, d \geq 1$, an ideal $J$ on $Z$ and a Cartier divisor $B$ on $S$ such that `UPoinOnX` holds:

1. $Z$ is normal and projective over $F$, $i$ is a dense open immersion, and $\mathcal{O}_Z(1)$ is ample;
2. $f^*\mathcal{O}_Z(1) \cong \omega_Y^{N}$ for each model $Y$ with a map $f \colon Y \to Z$ that extends $i$, if $\omega_Y$ is a line bundle;
3. a point of $X_F$ over the fraction field of a local domain $R$ extends to an $R$-point of $Z$ if its universal object extends to a semi-abelian scheme over $R$ with degeneration data;
4. $J$ lives on the boundary. Its valuations are those of $d\varphi$ (`UValOn`): along a point over a discrete valuation ring with uniformizer $\varpi$ whose degeneration is monomial with form $\beta$, $J$ pulls back to $(\varpi^{d\varphi(\beta)})$;
5. $\pi$ is a normalized blowup of $J$ (`IsNormBl`: a finite birational map followed by the blowup), $S$ is projective, $j$ is a dense open immersion with $\pi \circ j = i$ and $\pi^{-1}(i(X_F)) = j(X_F)$, and $B$ has ideal $J\mathcal{O}_S$;
6. $\pi^*\mathcal{O}_Z(k)(-B)$ is ample for all large $k$.

Also, $j$ satisfies `SepB`:

- the input is a local domain $V$ with degeneration data over it that are monomial in elements $s_1, \dots, s_m$ of the maximal ideal, with forms from a cone of $\varphi$ (`MonoFam`), and a $V$-point of $S$ through $j$;
- add units $s_{m+1}, \dots, s_{m+N}$ so that the trivializations $\tau$ of the data are monomials in all the $s_i$ (`TauIn`);
- let $V \to K$ be a map to an algebraically closed field whose point of $S$ is defined over an algebraically closed subfield $k_0$;
- then (`SepAtB`) $s_1, \dots, s_m$ vanish in $K$, and the abelian part comes from $k_0$. If the data descend to a subring that maps into $k_0$ (`FromBase`), then the units take values in $k_0$.

## Proof

1. `unitary_integral_compactifications_exist` gives `UCompact`: a Dedekind domain $o \subset F$ of finite type over $\mathbb{Z}$ with fraction field $F$, and a normal projective $Z_o$ over $o$ with an ample bundle. It also gives clauses 2 and 3 over $o$.
2. `unitaryCompactification_exists_boundary_ideal` gives $d$ and a boundary ideal $J_0$ on $Z_o$ with the valuations of $d\varphi$.
3. Let $Z = Z_o \times_o F$ and $J = J_0 \mathcal{O}_Z$. Clause 1 follows from `generic_fibre_normal_projective_ample_charZero`. The valuations pass to $J$, and later to $B$, by `idlAlong_comap_eq`.
4. `exists_normBl` gives $\pi$ and $B$, with $\pi$ an isomorphism over $i(X_F)$. This defines $j$.
5. Clause 2 follows from `lbIso_pull_comp`, and clause 6 from `ample_twist_of_blowup`.
6. `SepB` is `separation_normalizedBlowup_unitaryCompactification`. This is the only step that uses `NoSelfInt`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [UnitaryToroidalSeparationOfBase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryToroidalSeparationOfBase.lean#L23). The statement `UPoinOnX` is in [SpecializesGenericImage.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SpecializesGenericImage.lean#L153), and `SepB` is in [FromBaseAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FromBaseAlt.lean#L45). Step 6 cites `USep.sepB_of_normBl`. The ring in clause 4 has `CDvr`, which by its name is a complete discrete valuation ring. We have not unfolded `CDvr`, `Gens`, `Good`, `val` or `gm`.
