---
id: exists-bot-dat-pin-of-placed-of-framed
title: One central pin for all placed framed Bessel data
kind: theorem
decl: GlobalTheory.MiTop.exists_botDat_pin_of_placed_of_framed
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.OneCentralPin
covers: 1055
status: drafted
drafted_by: writer@claude
---
This theorem finds one central adelic element $z$ that pins a bottom datum on every placed and framed Bessel datum at once. Its only user is the restatement [`exists_botDat_of_placedP_framed`](/entry/exists-bot-dat-of-placed-p-framed/), which [`famAllQ_of_allTrue_alt`](/entry/fam-all-q-of-all-true-alt/) calls in step 1 of its proof. There the element $z$ becomes the first part of `FamilyAllConditions W`. That theorem is part of the multiplicity condition in branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Let $D$ be a datum of type `D7` and $W$ a real package over $D$ (`RealPackAlt`). For a hermitian space $V$ of $D$, `GA D V` is the group of invertible matrices over $\mathbb A_F \otimes_F E$ that preserve the Gram matrix of $V$, that is, the adelic [[unitary group|0R9R0Y1HDK]] of $V$. Its subgroup `GfC V` is the kernel of the projection to the archimedean component. We write $G(V)$ and $G_f(V)$. The spaces $X_0$ and $Y_0$ are `D.sp.X 0` and `D.sp.Y 0`.

A bottom datum $d$ for a word $u$ is a Bessel datum $\mathcal B$ (`SBes`) on $X_0$, elements $b, k \in G(Y_0)$ and $a_0, a \in G(X_0)$. For $z \in G(Y_0)$, `d.Pin z` says:

1. $\mathcal B$ is adapted to the weight of `W.S.tr u`, and $a_0$ is a transport adelic correction;
2. $a \in G_f(X_0)$ and $a$ is central in $G(X_0)$;
3. $k$ is in the level set $J$ = `rJ_z W`;
4. $\iota_{\mathcal B}(a_0 a)\, b = x_u \, z \, t_S \, k$, where $\iota_{\mathcal B} \colon G(X_0) \to G(Y_0)$ is the embedding `embA` of $\mathcal B$, $x_u$ is the element `(iotaX ...).symm (1, xu u)` and $t_S$ is the element `W.Q.tS`.

$\mathcal B$ is *framed* if there are $\mu \neq 0$ and $\lambda = \pm g$ (with $g$ a fixed element `X.B.g` of $E$) such that the vector of $\mathcal B$ is $\mu$ times a fixed vector `zR u`, and its two frames $e, e'$ are $\mu\lambda^{r_S - a}$ and $(\overline{\mu\lambda^{r_S - a}})^{-1}$ times fixed frames. $\mathcal B$ is *placed* for a family character $f$ (`PlacedConditions f B`) if there are a local field, vector data $v$, type data $o$ and local groups $G_i$ with eight conditions, one of them a local bottom compatibility of $f$, $\mathcal B$, $v$, $o$, $G$.

**Theorem.** Assume `PackageHypotheses W` and $1 \le r_S$. Then there is $z \in G_f(Y_0)$, central in $G(Y_0)$, such that for each word $u$, each family character $f$ and each placed and framed $\mathcal B$ there is a bottom datum $d$ with $d.\mathcal B = \mathcal B$, $d.b = f.g.b_0$ and `d.Pin z`.

## Proof

If no placed and framed $\mathcal B$ exists, take $z = 1$; the claim is empty. Otherwise fix one, $(u_0, f_0, \mathcal B_0)$.

1. `exists_isAt_of_placed_framed` gives $a_0, a$ such that the translation element $t_0 = x_{u_0}^{-1}\, \iota_{\mathcal B_0}(a_0 a)\, f_0.g.b_0$ "matches" $(J, \chi)$, where $\chi$ is the character `realCharacter W`. We have not unfolded `Matches`.
2. The field `bot` of the package hypotheses, through `botHyp_match_alt`, says that $z' t_S$ matches for each central $z' \in G_f(Y_0)$. So $t_S$ matches.
3. `matching_translates_bottom_alt` compares $t_0$ and $t_S$. It gives a central $z \in G_f(Y_0)$, a central $c \in G_f(X_0)$ and $k_0 \in J$ with $t_0 = x_{u_0}^{-1} \iota_{\mathcal B_0}(c)\, x_{u_0}\, z\, t_S\, k_0$.
4. Replace $a$ by $c^{-1} a$. Since $c$ is central, the new translation element is $z t_S k_0$. It matches by step 2 and the helper `matches_mul_of_mem_rJ'` (line 30): matching is stable under right multiplication by $J$.
5. Now let $(u, f, \mathcal B)$ be placed and framed. `exists_isAt_of_placed_framed` and `placed_bessel_compatibility_alt` give $b_0, a_1$ and $k \in J$ such that the translation element of $(f, \mathcal B, b_0, a_1)$ is $z t_S k_0 k$.
6. Put $d = (\mathcal B, f.g.b_0, b_0, a_1, k_0 k)$. Clause 1 of `Pin` comes from the placed conditions and from step 5; clauses 2 and 3 from step 5 and $k_0 k \in J$; clause 4 is the identity of step 5 multiplied by $x_u$ on the left.

## In the Lean code

The theorem is at [OneCentralPin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OneCentralPin.lean#L41). `BottomData` and `Pin` are in [FormsAtZero.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FormsAtZero.lean#L40), `Framed` in [Framed.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/Framed.lean#L15), and `GA`, `GfC` in [IsAutFunDef.lean](lean:Formalism/LocalToGlobal/BesselHermitianTheta/IsAutFunDef.lean#L15). The lemmas it calls:

- `exists_isAt_of_placed_framed`, twice;
- `botHyp_match_alt`;
- `matching_translates_bottom_alt` and `placed_bessel_compatibility_alt`, the two users of $1 \le r_S$;
- `matches_mul_of_mem_rJ'`, in the same file.

The element $z$ comes from one reference datum $(u_0, f_0, \mathcal B_0)$, chosen by `by_cases` with classical logic. The case with no placed framed datum gives $z = 1$ with an empty claim.
