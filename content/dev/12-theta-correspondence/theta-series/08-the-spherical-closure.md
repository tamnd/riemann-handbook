---
title: The spherical closure
decls:
  - PositivityTheory.Sph.Tr.endAB_sph
  - PositivityTheory.Sph.Tr.closeSph
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The spherical closure

This section proves the two statements of the [theta matching chapter](/proof/theta-matching/): the [agreement of theta integrals](/step/theta-integrals-agree-def/) and [local matching](/step/local-matching-def/). It takes fourteen statements as assumptions, local ones at each kind of place and global ones on reduction theory, Weil representations, [[Eisenstein series|3NZBZXYWAJ]] and the Siegel-Weil formula. The first theorem is the endgame: two matched theta integrals are proportional as soon as one part of their constant terms is proportional. The second theorem assembles everything. The [spherical forms](/entry/sph-fun-of-mod-st/) of the previous section give the local input at the inert places, and the result feeds the [theorem on theta integrals and local matching](/entry/theorem-k-head2/) of the chapter on Howe duality.

### The assumptions

We keep the triples of the previous section: Hermitian spaces $V$, $V'$ of dimensions $a$, $a'$ and $W$ over a CM extension $E/F$, Hecke characters $\alpha, \beta$ with a finite set $T$ of places, and [[Weil representations|H3Q2703KKV]] $\omega$ of $U_V \times U_W$ and $\omega'$ of $U_{V'} \times U_W$. We do not unfold the statements below; we say in words what each one asserts.

1. (Ramified places.) For each finite place $v \in T$ there are local maps from the local Schwartz spaces of $\omega_v$ and $\omega'_v$ onto one irreducible nontrivial space. They kill the coinvariants, respect the action of $U_W(F_v)$, and satisfy a zeta condition.
2. (Split places.) The same for the finite places outside $T$ that split in $E$, with the vacuum vectors mapped to the same vector.
3. (Inert places.) The same for the finite places outside $T$ that are inert in $E$.
4. (Spherical or irreducible.) At each place, each of $\omega$ and $\omega'$ is spherical or irreducible.
5. (Multiplicity one at ramified places.) At $v \in T$, two local equivariant maps of a given type between the quotients of a triple and of a smaller triple are proportional when the first is not zero.
6. (Kernels.) If the local Weil representations agree with their explicit models, then at the good places the kernels of matched local maps are the coinvariant spaces.
7. (Coinvariants at one place.) If local maps as in 1 to 3 exist at all finite places, then a statement on coinvariants inside a subspace at one place holds.
8. (Real places.) Matched local maps exist at the infinite places.
9. (Derivatives.) On the polynomial Fock space, the operators of $\omega$ along one-parameter subgroups are differentiable at $0$, with derivative in that space.
10. (Lie algebra.) The Weil representation acts on the Fock model by a given second order formula.
11. (Siegel sets.) Reduction theory for the adelic unitary group: an Iwasawa decomposition $g = p a k$, and a closed Siegel set whose rational translates cover the group.
12. (Existence of Weil representations.) Weil representations exist for each good model and each suitable pair of Hecke characters.
13. (Eisenstein series.) A statement on Siegel Eisenstein series of [the Siegel-Weil chapter](/proof/siegel-weil/).
14. (Siegel-Weil.) A standard form of the [Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula).

### The endgame

For a matched pair $(\Phi, \Phi')$ of test functions, with $\Phi'$ in a fixed subspace of Schwartz functions, write $I(\Phi)$ and $I'(\Phi')$ for the two theta integrals, as functions on $U_W$ over the adeles. Let $H'$ be a plane adapted to $W$, spanned by isotropic vectors $x$ and $y$. A *Levi element of scale $1$* is an $m$ with $m x = x$ and $m y = y$ that preserves the complement of $H'$. A *split* of a function $f$ on $U_W$ is a pair $(f_a, f_b)$ such that $f_a + f_b$ is the constant term of $f$ along $H'$, and $f_a$ and $f_b$ transform under the Levi subgroup by $\alpha |\cdot|^{a'/2}$ and $\beta |\cdot|^{a/2}$. The datum has two integers $p$ and $q$, which we do not unfold.

**Theorem 3.8.1 (Endgame).** Assume 1 to 3, 6, 9, 10, 11, 12, 13 and 14. Fix a matched datum, an adapted plane $H'$ and $c \in \mathbb{C}$.

- If $q \ge 1$, and $f_b(m) = c f'_b(m)$ for all matched pairs $(\Phi, \Phi')$, all splits $(f_a, f_b)$ of $I(\Phi)$ and $(f'_a, f'_b)$ of $I'(\Phi')$, and all Levi elements $m$ of scale $1$, then $I(\Phi) = c\, I'(\Phi')$ for all matched pairs.
- If $q = 0$ and $p \ge 1$, the same holds with $f_a, f'_a$ in place of $f_b, f'_b$.

Lean: `PositivityTheory.Sph.Tr.endAB_sph`

*Proof.* From the assumptions we get the facts that the argument needs: 1 to 3 give local maps at all finite places, 10 gives matched maps at the real places, 6 gives the kernels and the existence of matched pairs, 11 and 9 give rapid decay on Siegel sets, 14 gives the Siegel-Weil formula for anisotropic spaces, 13 gives the continuation of the Eisenstein series, and 12 gives the theta towers.

Put $f = I(\Phi) - c\, I'(\Phi')$. Then $f$ is a theta integral of the same kind, and it has the split $(f_a - c f'_a, f_b - c f'_b)$. Matched pairs stay matched under right translation by $U_W$, and a split of $I(\Phi)$ translates to a split of the translate. So the hypothesis holds at every right translate. With the Iwasawa decomposition, this extends the vanishing of one part from the Levi elements of scale $1$ to the whole group.

In the first case the $\beta$ part of $f$ is $0$, so the constant term of $f$ transforms by $\alpha |\cdot|^{a'/2}$ only. We show by induction on $p$ that such an $f$ is $0$. For $p = 0$ the base tower and a base case give $f = 0$. For $p + 1$ the tower of codimension two lowers $a$ by $2$ and $p$ by $1$, and the induction hypothesis applies. In the second case the $\alpha$ part of $f$ is $0$, and since $q = 0$ and $p \ge 1$ the $\beta$ part is $0$ as well. So the constant term of $f$ along $H'$ is $0$, and $f = 0$ by an argument with cusp forms along the line of $x$ and their orthogonal complements, whose inputs we do not unfold. $\square$

### The closure

**Theorem 3.8.2 (Spherical closure).** Assume 1 to 14. Then the [agreement of theta integrals](/step/theta-integrals-agree-def/) and [local matching](/step/local-matching-def/) hold.

Lean: `PositivityTheory.Sph.Tr.closeSph`

*Proof.* Local matching uses only the local assumptions. By 1 to 3 local maps exist at all finite places, and with 8 they give matched local data at every place.

For the agreement of theta integrals we need three things: the theta integrals decay, the kernels of matched maps are the coinvariant spaces, and a family of local and global facts holds. The decay comes from the Siegel sets 11. The kernels come from 6, since the local Weil representations do agree with their explicit models. In the family, the nonvanishing comes from the [doubling](/learn/theta/#the-doubling-method) integral and the towers of 12. With 13, 14 and a factorization, which uses 4, 9 and 7, it gives a nonzero constant for the base case $p = q = 0$. The local facts at all places come from the multiplicity one statements, at the unramified places, at the ramified places by 5, and at the infinite places. The [endgame](/entry/end-ab-sph/) gives the two proportionality statements. These facts together give one nonzero constant of proportionality for each matched pair and the two recursion laws for the constants, and so the agreement of theta integrals. $\square$

In the [first use of the closure](/entry/theorem-k-head2-of-mod/), all assumptions except 3, 13 and 14 are proved outright, and 3 is proved from the [spherical forms](/entry/sph-fun-of-mod-st/) with the global index formula as an assumption. The [second use](/entry/theorem-k-head2/) removes that assumption by the [global index formula](/entry/mod-st2/). So only 13 and 14 remain as assumptions.

**Remark 3.8.3 (Formalization).** The endgame is [EndCore.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/SphericalClosure/EndCore.lean#L64) and the closure is [CloseSph.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/SphericalClosure/CloseSph.lean#L28). The assumptions are, in order, `FinRam`, `FinSplit`, `FinInert`, `SphTri`, `RamifiedMultiplicityOne`, `DictSt → KCoinv`, `KFin → SoCoinv`, `KReal`, `ArchLie`, `LieSecond`, `SiegelSetUnitary`, `WeilEx`, `EisBL` and `SiegelWeilStd`; the two conclusions are `ThetaIntegralsAgree` and `LocalMatching`, and the endgame gives `EndA` and `EndB`. Most of these statements are not unfolded here, and nor are the integers $p$, $q$. The premises of assumptions 6 and 7 are proved inside the closure itself (CloseSph.lean L52 and L132), so the two implications could be plain statements. Assumption 8 is redundant: the endgame derives it from 10 (EndCore.lean L146). Assumption 4 is used only once, at L88. The matching half of the conclusion is almost a restatement of 1, 2, 3 and 8. Lines 129 to 131 of CloseSph.lean only rename hypotheses, and the same terms are built twice (L75 and L84, L182 and L185, and the endgame at L188 and L190). In EndCore.lean, lines 147 to 149 only rename, `coneFac_of` is applied twice to the same arguments (L178 and L179), so is `siegelWeilAniso_of` (L205 and L220), and the tower of codimension two is filled by a fact named `TowerA2`.

## Notes and references

This chapter feeds two parts of the proof. The [theta series at a level](/entry/level-theta-span/) span the bounded forms, and the step [EveryCharacter from the literature](/step/every-character-of-literature/) uses this. The [spherical closure](/entry/close-sph/) and the [global index formula](/entry/mod-st2/) prove the [theorem on theta integrals and local matching](/entry/theorem-k-head2/) of the chapter on Howe duality. It gives the step [theta integrals agree and local matching](/step/theta-integrals-agree-and-local-matching-of-literature/), and through [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/) it enters the same step. The [change of representative](/entry/theta-change-of-rep-root-of-unity-of-chart-independence/) of the theta function feeds the [change of frame](/entry/short-rule-change-mat/) of Volume 15. The definite Siegel-Weil formula is used inside this chapter, by the kernel identity.

The transformation law of theta functions follows Mumford and Igusa, and the Hermitian case follows Shimura. The definite Siegel-Weil formula is due to Siegel and, in adelic form, to Weil; the proof here by Hecke operators and a contraction replaces the adelic proof. The span of theta series with harmonic coefficients goes back to Hecke and Eichler, in the form of Kashiwara and Vergne. The doubling method is that of Gelbart, Piatetski-Shapiro and Rallis. The local theta correspondence and the unramified computations are those of Howe, Rallis, and Mœglin, Vignéras and Waldspurger, and the regularized Siegel-Weil formula is that of Kudla and Rallis and, for unitary groups, of Ichino. Here the spherical part is proved by an index formula in a Siegel parabolic, and the global comparison is assembled from fourteen assumptions.

- D. Mumford, *Tata Lectures on Theta I*, Progr. Math. 28, Birkhäuser (1983), Ch. II.
- J.-I. Igusa, *Theta Functions*, Grundlehren 194, Springer (1972).
- H. Klingen, *Introductory Lectures on Siegel Modular Forms*, Cambridge Stud. Adv. Math. 20 (1990).
- G. Shimura, *Arithmetic of unitary groups*, Ann. of Math. 79 (1964), 369-409.
- C. L. Siegel, *Über die analytische Theorie der quadratischen Formen*, Ann. of Math. 36 (1935), 527-606.
- A. Weil, *Sur la formule de Siegel dans la théorie des groupes classiques*, Acta Math. 113 (1965), 1-87.
- M. Kashiwara and M. Vergne, *On the Segal-Shale-Weil representations and harmonic polynomials*, Invent. Math. 44 (1978), 1-47.
- R. Howe, *θ-series and invariant theory*, Proc. Sympos. Pure Math. 33, Part 1 (1979), 275-285.
- S. Rallis, *Langlands' functoriality and the Weil representation*, Amer. J. Math. 104 (1982), 469-515.
- S. Gelbart, I. Piatetski-Shapiro and S. Rallis, *Explicit Constructions of Automorphic L-Functions*, Lecture Notes in Math. 1254 (1987).
- C. Mœglin, M.-F. Vignéras and J.-L. Waldspurger, *Correspondances de Howe sur un corps p-adique*, Lecture Notes in Math. 1291 (1987).
- S. S. Kudla, *Notes on the local theta correspondence*, lecture notes (1996).
- S. S. Kudla and S. Rallis, *A regularized Siegel-Weil formula: the first term identity*, Ann. of Math. 140 (1994), 1-80.
- A. Ichino, *A regularized Siegel-Weil formula for unitary groups*, Math. Z. 247 (2004), 241-277.
