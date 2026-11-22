---
id: abelian-de-rham
title: The first de Rham cohomology of an abelian scheme
kind: theorem
decl: PositivityTheory.DualRT.abelianDeRham
module: Development.WeilBound.CoreStatements.AutomorphicKernels.DualAbelianScheme.AbelianDeRhamDuality.AbelianDeRhamDuality
covers: 1213
status: drafted
drafted_by: writer@claude
---
This theorem proves five facts about $H^1_{\mathrm{dR}}$ of an abelian scheme over any commutative ring. The proof of [EveryCharacter from Row0b](/step/every-character-of-row/) reaches it through two wrappers that ignore their argument: `abelian_de_rham_of_literature`, a helper of the [literature structure](/step/every-character-of-literature/), and `abelian_de_rham_of_open`, which takes the `OpenImageCondition` of [VWin from Row0b](/step/vwin-of-row/). Below this theorem are 1,213 declarations.

## Statement

Let $R$ be a commutative ring and $A$ an abelian scheme over $\operatorname{Spec} R$ of relative dimension $g$. Let $H^i_{\mathrm{dR}}$ be `FirstDeRham` and `SecondDeRham`: the cohomology of the structure sheaf on the code's site of divided power thickenings over $R$, with the zero ideal. Let $P \subseteq H^1_{\mathrm{dR}}$ be the primitive classes ($m^*c = p_1^*c + p_2^*c$), $F^1$ the kernel of $H^1_{\mathrm{dR}} \to H^1(A, \mathcal{O}_A)$, $D = \operatorname{Hom}_R(P, R)$ (`HdR A`), and $\operatorname{Fil} \subseteq D$ the annihilator of $P \cap F^1$.

**Theorem.** For all such $R$, $A$, $g$:

1. *Free.* $P = H^1_{\mathrm{dR}}$. It is finite projective of rank $2g$ at each prime, and cup product gives $\bigwedge^2 H^1_{\mathrm{dR}} \cong H^2_{\mathrm{dR}}$.
2. *Hodge.* Each $h \in D$ comes from a unique tangent vector $v \colon \operatorname{Spec} R[\varepsilon] \to A$, in the sense $h(\mathrm{cl}\, f) = f(v)$ for each 1-form $f$ with primitive class, and each tangent vector comes from some $h$ (`LieExact`). $P \cap F^1$ is a direct summand of $P$, projective of rank $g$.
3. *Base change.* For $A' = A \times_R R'$, pullback gives a bijection $R' \otimes_R P \to P'$, and $P' \cap F^1$ is spanned by the image of $P \cap F^1$.
4. *Rigidity.* Let $I \subseteq R$ carry nilpotent divided powers $\kappa$ (`IsNilDP`) and $A_0 = A \times_R R/I$. Pullback from $P$ to the primitive crystalline classes of $A_0$ relative to $(R, I, \kappa)$ is bijective.
5. *Duality.* Let $L$ be a line bundle on $A$ and $\psi(x, y) = \sum_k \bigl(x(a_k)y(b_k) - x(b_k)y(a_k)\bigr)$ on $D$, with $a_k, b_k \in P$ and $\sum_k a_k \cup b_k$ the Chern class of $L$ (`IsPolForm`). Then $\psi(\operatorname{Fil}, \operatorname{Fil}) = 0$. If the only point $x$ with $t_x^*L \otimes L^{-1}$ trivial is the unit (`KTriv`), $\psi$ is perfect.

For parts 1 to 3 see Berthelot, Breen and Messing, *Théorie de Dieudonné cristalline II*, LNM 930 (1982), Section 2.5.

## Proof

1. **Parts 1 to 3.** [`abelianHodgeDeRham`](/entry/free-abelian-hodge-de-rham/) gives the Hodge-de Rham statement for Čech-de Rham hypercohomology. `abelianDeRhamStructure_of_page` turns it into parts 2, 3 and most of part 1, with `crystallineSmoothLift_of_relations`, which compares crystalline and Čech-de Rham $H^1$ and $H^2$. `abelianDeRhamStructure_toFree` adds $P = H^1_{\mathrm{dR}}$.
2. **Part 4.** `rigid_of_free_of_crystallineDeRham` uses part 1 and `Adr.crystallineDeRham`: for smooth, separated, quasi-compact $X$ over $R$, pullback from $H^i_{\mathrm{dR}}(X/R)$ to the crystalline $H^i$ of $X \times_R R/I$ is bijective for $i = 1, 2$.
3. **Part 5.** `surjAll_of_hodge` shows that a map `toP` from $H^1_{\mathrm{dR}}$ to `H1OnPoints` (not unfolded) is onto. Then `duality_of_surjAll` gets isotropy from `orth_of_surj` and perfectness from `perfect_ring`.

## In the Lean code

The theorem is in [AbelianDeRhamDuality.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/DualAbelianScheme/AbelianDeRhamDuality/AbelianDeRhamDuality.lean#L20), with `surjAll` and `duality` above it. The statement is in [CrysToDRBijective.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/CrysToDRBijective.lean#L65).

Odd points:

- A round trip. `page_of_hodge` turns `AbelianHodgeDeRham` into `AbelianDeRhamPage`, and `abelianDeRhamStructure_of_page` turns it back with `abelianHodgeDeRham_of_page`.
- `abelianDeRhamStructure_crystallineDeRham_of_hypotheses` also proves `CrystallineDeRham`, but only its first component is kept. Part 4 uses a second proof, `Adr.crystallineDeRham`.
- `abelianDeRham` and `duality` each build the same value `hS`.
- The namespaces (`PositivityTheory`, `FubiniStudyChowHeightFormula₂`, folder `AutomorphicKernels`) say nothing about the content. A different theorem, `CrystallinePoints.Pd.abelianDeRham` in [PoincareDeRhamDualityOfCube.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/PoincareDeRhamDuality/DeRhamPerfectPairing/PoincareDeRhamDualityOfCube.lean#L45), has the same short name.
- `IsChern` is not unfolded here.
