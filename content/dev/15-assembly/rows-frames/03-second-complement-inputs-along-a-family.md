---
title: Second complement inputs along a family
decls:
  - GlobalTheory.familySecondComplementInputs_of_tuSize_of_dGamSize
  - GlobalTheory.T.admissibleComplementTwo_along_family
  - GlobalTheory.admissibleConstants_closed_under_sizeBounds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Second complement inputs along a family

This section proves that the eight inputs of the second complement bound hold along a family of data, from two size bounds on the family. The second complement bound is a bound on the isotypic rank of the second complement of a datum. It is used by [the second complement at the constructed points](/entry/division-second-complement-constructed-points/) of Volume 13, which needs the inputs for each family of a class that is closed in the sense below. The proof only collects six eventual bounds, proved elsewhere, and takes the largest of their thresholds.

A *family* with parameter $\varepsilon$ gives, for each real $x$ above a start point $x_1$ and each index $i$ in a finite set $I(x)$, a datum $D(x, i)$ of the main construction with size data $L(x, i)$ and error data. We write $m$ for the rank parameter of the datum and $\mathcal{L}$ for the logarithmic scale of the size data.

The *second complement inputs* of a datum $D$ with size data $L$ and constants $C_{\deg}, C_g, C_T, C_G, C_d, C_I$ are the following eight statements:

1. the level primes of $D$ are not type primes;
2. the norm decomposition condition holds;
3. the degree count bound holds with constant $C_{\deg}$;
4. the type prime sizes are bounded with constants $C_{\deg}$ and $C_g$;
5. the level prime budget holds with constant $C_T$;
6. the stabiliser logarithm bound holds with constant $C_G$;
7. the discriminant offset bound holds with constant $C_d$;
8. the inert prime loss bound holds with constant $C_I$.

When they hold, $C_g \geq 0$ and the error data are large, the isotypic rank of the second complement is at most $2 C_g + C_T + C_G + C_d + C_I$. The inputs hold *along the family* if there are constants as above with $C_g \geq 0$ and a threshold $x_0$ such that they hold for $D(x, i)$ for all $x \geq x_0$ with $x > x_1$ and all $i \in I(x)$.

The two size bounds are these. The family has the *level size bound* if there is $x_0$ such that for $x \geq x_0$ and every $i$, the level data of $L(x, i)$ satisfy the lower bound on levels, and every level $T_u$ of a member $u$ of $D(x, i)$ satisfies
$$\log T_u \leq C_{Tu}\, m\, \mathcal{L},$$
where $C_{Tu}$ is the constant of the family. The family has the *discriminant size bound* if there are $C$ and $x_0$ such that for $x \geq x_0$ and every $i$ the datum $D(x, i)$ has the discriminant factor bound with constant $C$.

**Theorem 7.3.1 (Inputs from the size bounds).** Let $0 < \varepsilon < \tfrac{1}{52}$ and let a family with parameter $\varepsilon$ have the level size bound and the discriminant size bound. Then the second complement inputs hold along the family.

Lean: `GlobalTheory.familySecondComplementInputs_of_tuSize_of_dGamSize` (also `GlobalTheory.T.admissibleComplementTwo_along_family`).

*Proof.* Inputs 1 and 2 hold for every datum of the main construction. Each of the other six inputs holds eventually along the family, by six results proved apart from this chapter:

- the degree count bound holds for $x \geq x_d$ with a constant $C_{\deg}$, for $0 < \varepsilon < \tfrac{1}{52}$;
- with this $C_{\deg}$, the discriminant size bound gives the type prime size bound for $x \geq x_g$, with a constant $C_g \geq 0$;
- the level size bound gives the level prime budget for $x \geq x_T$;
- the two size bounds together give the stabiliser logarithm bound for $x \geq x_G$;
- the discriminant offset bound holds for $x \geq x_D$;
- the inert prime loss bound holds for $x \geq x_I$.

Put
$$x_0 = \max(x_d, x_g, x_T, x_G, x_D, x_I).$$
For $x \geq x_0$ each of the six thresholds is at most $x$, so all eight inputs hold for $D(x, i)$ for each $i$, with the constants $C_{\deg}, C_g, C_T, C_G, C_d, C_I$. $\square$

A class $\mathcal{C}$ of families is *closed* for a property $Q$ of families if there is $\varepsilon_1 > 0$ with this property: for each $\varepsilon \in (0, \varepsilon_1]$ there are transported constants $K$ such that each family with parameter $\varepsilon$ in $\mathcal{C}$ that is large for $K$ and a height constant has $Q$. This is the notion [Closed](/step/closed-def/) of [the unitary hypotheses](/proof/unitary-hypotheses/).

**Theorem 7.3.2 (Closed under the size bounds).** Let $\mathcal{C}$ be a class of families such that each family in $\mathcal{C}$ has the level size bound and the discriminant size bound. Then $\mathcal{C}$ is closed for the property that the second complement inputs hold along the family.

Lean: `GlobalTheory.admissibleConstants_closed_under_sizeBounds`.

*Proof.* Take $\varepsilon_1 = \tfrac{1}{100}$. Let $0 < \varepsilon \leq \tfrac{1}{100}$ and let $K$ be the transported constants with all entries $0$. Let a family with parameter $\varepsilon$ lie in $\mathcal{C}$. Then $\varepsilon < \tfrac{1}{52}$, and the family has the two size bounds. The last theorem gives the inputs along the family. $\square$

**Remark 7.3.3 (Formalization).** The family is `FamP eps` and the class is `FamClass`. The inputs are `SecondComplementInputs` and `FamilySecondComplementInputs` in [WeightDegreeSizes.lean](lean:Formalism/SharpRestriction/Divisibility/WeightDegreeSizes.lean#L673), and `Closed`, `TuSize` and `DGamSize` are in [ParamsHeightRankConstant.lean](lean:Formalism/SharpRestriction/ParamsHeightRankConstant.lean#L159). The six eventual bounds are `T.exists_degreeCountBound_of_eps_lt_one_div_52`, `T.typePrime_sizes_le_budget_family`, `T.admissible_off_type_family_bound`, `T.exists_const_stabiliserLog_bound_along_family`, `T.offDiagonalRamified_bound_along_family'` and `T.inertPrimeLossBound_eventually`; we read their statements, not their proofs. Four of them also return a sign condition on their constant, which the proof drops with `-`. Inputs 1 and 2 come from the field `T_ne_g` of the datum and from `T.normDecompositionCond_famP`. In the closed theorem the transported constants, the largeness hypothesis and the height constant are not used: the proof builds $K$ with every field $0$ and ignores both the largeness and the height constant. The value $\tfrac{1}{100}$ could be any number below $\tfrac{1}{52}$. The property is stated without the height constant, as `fun Fm _ => FamilySecondComplementInputs Fm`.
