---
title: Algebraisation of formal morphisms and formal schemes
decls:
  - PositivityTheory.FormalThickening.formalAlgebraisation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Algebraisation of formal morphisms and formal schemes

This section proves Grothendieck's existence theorem in two forms, over a Noetherian ring $R$ that is complete for an ideal $I$. The first form says that a compatible family of morphisms from the thickenings of a proper $R$-scheme $X$ to a separated $R$-scheme $Z$ of finite type comes from exactly one morphism $X \to Z$. The second form says that a compatible family of proper schemes over the rings $R/I^{e+1}$, with a compatible family of line bundles that is relatively ample at the bottom, comes from one proper $R$-scheme with a relatively ample line bundle. The proof reduces both forms to the existence theorem for closed subschemes. The result is the published statement of [the literature entry](/entry/formal-algebraisation-of-literature/) of Volume 15. There it is used to pass from formal data near a boundary point to algebraic data.

### Thickenings

Let $R$ be a Noetherian ring and $I$ an ideal for which $R$ is $I$-adically complete. For $e \ge 0$ put $R_e = R/I^{e+1}$. Let $t_e : \operatorname{Spec} R_e \to \operatorname{Spec} R$ and $\tau_e : \operatorname{Spec} R_e \to \operatorname{Spec} R_{e+1}$ be the closed immersions given by the quotient maps.

**Definition 4.7.1 (Thickenings of an $R$-scheme).** Let $X$ be an $R$-scheme. A system of thickenings of $X$ is a family of $R_e$-schemes $Y_e$ with morphisms $b_e : Y_e \to X$ and $\beta_e : Y_e \to Y_{e+1}$ such that each square
$$\begin{array}{ccc} Y_e & \xrightarrow{b_e} & X \\ \downarrow & & \downarrow \\ \operatorname{Spec} R_e & \xrightarrow{t_e} & \operatorname{Spec} R \end{array}$$
is a pullback square and $b_{e+1} \circ \beta_e = b_e$.

So $Y_e$ is $X \times_R R_e$, and the $\beta_e$ are the inclusions of the thickenings. A compatible family of morphisms to an $R$-scheme $Z$ is a family $f_e : Y_e \to Z$ of $R$-morphisms with $f_{e+1} \circ \beta_e = f_e$.

**Definition 4.7.2 (Line bundle, relatively ample).** A line bundle on a scheme $Y$ is given by an open cover $(U_i)$ and units $g_{ij} \in \Gamma(U_i \cap U_j, \mathcal{O}^\times)$ with $g_{ii} = 1$ and the cocycle condition $g_{ij} g_{jk} = g_{ik}$ on triple overlaps. An isomorphism of line bundles is a compatible family of units. A line bundle $\mathcal{L}$ on a scheme $A$ over $S$ is relatively ample if for every affine open $U \subseteq S$ there are $N \ge 1$ and sections $s_0, \dots, s_M$ of $\mathcal{L}^{N}$ over the preimage $A_U$ such that the open sets $D(s_i)$ where $s_i$ does not vanish are affine and cover $A_U$, and for each $i$ the ratios $s_j/s_i$ are regular on $D(s_i)$ and generate $\Gamma(D(s_i), \mathcal{O})$ as an $\mathcal{O}(U)$-algebra.

The second condition says that the sections $s_j$ define a closed immersion $A_U \to \mathbb{P}^M_U$: the line bundle has a very ample power over each affine open of the base.

### The theorem

**Theorem 4.7.3 (Grothendieck existence).** Let $R$ be a Noetherian ring, complete for an ideal $I$.

1. (Morphisms.) Let $X$ be a proper $R$-scheme, and let $Z$ be a separated, quasi-compact $R$-scheme, locally of finite type. Let $(Y_e, b_e, \beta_e)$ be a system of thickenings of $X$ and $(f_e)$ a compatible family of morphisms $Y_e \to Z$ over $R$. Then there is exactly one $R$-morphism $g : X \to Z$ with $g \circ b_e = f_e$ for all $e$.
2. (Schemes.) Let $Y_e$ be proper $R_e$-schemes and $\beta_e : Y_e \to Y_{e+1}$ morphisms such that each square with $\tau_e$ is a pullback, so that $Y_e = Y_{e+1} \times_{R_{e+1}} R_e$. Let $\mathcal{N}_e$ be line bundles on $Y_e$ with isomorphisms $\mathcal{N}_e \cong \beta_e^*\mathcal{N}_{e+1}$, and assume that $\mathcal{N}_0$ is relatively ample over $R_0$. Then there are a proper $R$-scheme $X$, a relatively ample line bundle $\mathcal{M}$ on $X$, and morphisms $b_e : Y_e \to X$ such that $(Y_e, b_e, \beta_e)$ is a system of thickenings of $X$ and $\mathcal{N}_e \cong b_e^*\mathcal{M}$ for all $e$.

Lean: `PositivityTheory.FormalThickening.formalAlgebraisation`

The proof uses three inputs, which are proved elsewhere in the development. The first is the existence theorem for closed subschemes ([Theorem 7.3.3 of Volume 3](/entry/grothendieck-existence-closed/)).

**Theorem 4.7.4 (Closed subschemes).** Let $P$ be a separated, quasi-compact $R$-scheme, locally of finite type, and let $C_e \subseteq P \times_R R_e$ be closed subschemes with $C_e = C_{e+1} \times_{R_{e+1}} R_e$, such that $C_0$ is proper over $R_0$. Then there is a closed subscheme $C' \subseteq P$, proper over $R$, with $C_e = C' \times_R R_e$ compatibly in $e$. For $P = \mathbb{P}^N_R$ the same holds without the properness assumption on $C_0$.

Lean: `GlobalTheory.T.grothendieck_existence_closed` (also `GlobalTheory.T.grothendieck_existence_closed_proj`)

**Theorem 4.7.5 (Isomorphism on thickenings).** Let $X$ and $C$ be $R$-schemes with $X$ proper, and let $p : C \to X$ be a proper $R$-morphism such that $p \times_R R_e$ is an isomorphism for every $e$. Then $p$ is an isomorphism.

Lean: `GlobalTheory.T.iso_of_thickenings`

The third input says that two morphisms $g, g' : X \to Z$, with $X$ proper and $Z$ separated, that agree on every $Y_e$ are equal.

*Proof.* Part 1, existence. Put $P = X \times_R Z$, a separated, quasi-compact $R$-scheme of finite type. Since $Z$ is separated, the graph of $f_e$ is a closed subscheme $C_e$ of $P \times_R R_e = Y_e \times_{R_e} (Z \times_R R_e)$, and these graphs are compatible in $e$. The bottom graph $C_0 \cong Y_0$ is proper over $R_0$, because $Y_0 = X \times_R R_0$. The closed subscheme theorem gives a closed $C' \subseteq P$, proper over $R$, with $C' \times_R R_e = C_e$. Let $p : C' \to X$ be the first projection. It is proper, since $C'$ is proper and $X$ is separated. Over each $R_e$, $p$ is the projection of the graph $C_e$ to $Y_e$, an isomorphism. By the second input, $p$ is an isomorphism. Put $g = q \circ p^{-1}$, with $q : C' \to Z$ the second projection. Then $g \circ b_e = f_e$.

Part 1, uniqueness. If $g'$ is a second such morphism, then $g' \circ b_e = f_e = g \circ b_e$ for all $e$, and the third input gives $g' = g$.

Part 2. Choose a power $\mathcal{N}_0^{d}$ with sections that embed $Y_0$ into a projective space, and lift sections of suitable powers $\mathcal{N}_e^{D}$ compatibly to all $e$. Sections of two consecutive multiples of the exponent are used, and products of them give a family $(z_j)$ of sections of $\mathcal{N}_e^{D}$ that is very ample on $Y_0$. Then the $z_j$ embed every $Y_e$ compatibly as a closed subscheme of $\mathbb{P}^m_{R_e}$. The projective case of the closed subscheme theorem gives a closed $X \subseteq \mathbb{P}^m_R$ with $X \times_R R_e = Y_e$. The scheme $X$ is proper over $R$. The line bundle $\mathcal{M}$ is built from $\mathcal{O}(1)$ on $X$ and the two consecutive powers, so that $b_e^*\mathcal{M} \cong \mathcal{N}_e$, and it is relatively ample because a power of it is $\mathcal{O}(1)$. $\square$

**Remark 4.7.6.** In the classical form (EGA III₁, §5.4), Part 1 says that the functor from proper $R$-schemes to proper formal schemes over $\operatorname{Spf} R$ is fully faithful, and Part 2 says that a proper formal scheme with an ample line bundle is algebraizable. Here formal schemes do not appear: a formal object is the family of its thickenings. Part 1 asks $Z$ only to be separated and of finite type; Part 2 asks for relative ampleness only at $e = 0$, and gives it on $X$.

**Remark 4.7.7 (Formalization).** The theorem only combines four lemmas: the existence and the uniqueness of morphisms, the algebraisation of schemes, and the closed subscheme theorem in two forms ([Development.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FormalAlgebraisation/Development.lean#L17)). The statement is the published statement, the conjunction of the two parts ([FormalAlgebraisation.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/FormalAlgebraisation.lean#L43)). A second proof of the same statement exists in the development (`GlobalTheory.formalAlgebraisation`, in Development/AbelianVarietyTheory/Proofs/DivisorProofs/FormalAlgebraisation.lean); it is separate from this one. The wrappers of the lemmas are proved by the tactic `first | exact ... | ...`, which tries three forms of the same term. For Part 2 we followed the main steps of FormalAlgebraisationSchemes.lean; we did not open the lemmas on lifting sections and on roots of line bundles that it calls.
