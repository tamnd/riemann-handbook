---
title: Rows and the period identity
decls:
  - GlobalTheory.T.main_theorem_published_inputs_third_alt_alt
  - GlobalTheory.miStarRow_alt_alt
  - GlobalTheory.T.main_theorem_published_inputs_variant_alt_alt
  - GlobalTheory.miStarRowClosing_alt_alt
  - GlobalTheory.T.main_theorem_published_results_final_alt_alt
  - GlobalTheory.Fam.miStar_row_alt_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rows and the period identity

This section proves the multiplicity row of [the open parameter statements](/entry/open0-of-unitary-group-hypotheses/). The multiplicity row asks that a period identity holds eventually at the selections of the good linked bundles. We reduce it in three steps. First, a row that holds at all points gives the multiplicity row. Second, the period identity at all good linked bundles follows from point conditions on the bundles. Third, at one bundle, the point conditions give a true package, and the period identity of a true package is [the Theorem of the next section](/entry/main-theorem-from-published-results-alt-alt-alt-alt-alt/).

We first make precise what "eventually" means. A *parameter* is a tuple $\kappa = (\varepsilon, C, c_D, c_h, C_5, c_6, C_b)$ of a real $\varepsilon$, a constant record $C$ and five reals. It is *positive* if $C_5, c_6, C_b > 0$.

**Definition 4.2.1 (Eventual statements).** A property $q$ of parameters holds *eventually* if there is $\varepsilon_0 > 0$ with the following property. For all $\varepsilon, C_8, C_5, c_6, C_b$ with $0 < \varepsilon \leq \varepsilon_0$, $\varepsilon < 1/52$ and $C_8 \geq 1$, there is $K_0$ such that for each standard constant record $C$ with $C_{\mathrm{pde}} = C_8$ and with $C$ large with respect to $K_0$, there is $c_1$ such that for each $c_D \geq c_1$ there is $c_2$ such that $q(\varepsilon, C, c_D, c_h, C_5, c_6, C_b)$ holds for each $c_h \geq c_2$. A property $P(\kappa, K)$ of parameters and contexts holds *eventually in the points* if eventually in $\kappa$ the following holds: if $\kappa$ is positive, there is $x_0$ such that $P(\kappa, K)$ holds for each context $K$ of $\kappa$ with $x_0 \leq x(K)$, where $x(K)$ is the point of the scale of $K$.

The order of the quantifiers is the order of the choices in [the unitary hypotheses](/proof/unitary-hypotheses/): first $\varepsilon$, then the constants, then $c_D$, then $c_h$, then the point.

**Definition 4.2.2 (Rows).** Let $Q$ be a predicate on bundles and $\Lambda$ a bundle linkage. Let $E(\kappa, D, O, c, b)$ be a property of a parameter, a datum $D$, an object $O$ over $D$, a real $c$ and a bundle condition $b$. The *eventual row* $\mathrm{RowE}(Q, \Lambda, E)$ is the statement that eventually in the points,

$$\text{for each bundle } \beta \text{ with } Q(\beta) \text{ and all } c, b \text{ with } \Lambda(K, \beta, c, b) : \quad E(\kappa, D_\beta, O_\beta, c, b).$$

For a property $H$ of selections, the *row* $\mathrm{Row}(Q, \Lambda, H)$ is the statement: there is $E$ such that $\mathrm{RowE}(Q, \Lambda, E)$ holds and $H(\mathcal{A}, \sigma)$ holds for each selection $(\mathcal{A}, \sigma)$ of $(Q, \Lambda, E)$.

A selection is a family $\mathcal{A}$ of bundles with a map $\sigma$ that sends each point, each index and each admissible choice to a bundle condition of $\mathcal{A}$. For a property $R$ of bundle conditions, $\mathrm{AtAll}(R)$ holds at $(\mathcal{A}, \sigma)$ if $R$ holds at every value of $\sigma$. The weaker property $\mathrm{EvW}(R)$ holds at $(\mathcal{A}, \sigma)$ if for each member $F$ of the closed family $W_3(\mathcal{A})$ and each admissible choice, $R$ holds at $\sigma(F, x, i)$ for all $i$ and all large $x$.

Now we define the period identity. Let $X$ be a coefficient space. It has a space $E_E$ of theta vectors with a subspace $E_{E,l}$, a set of words $u$, a set of tuples $t$ with a base tuple $\mu_0$, a theta map $\Theta_t$, row vectors and a period $P_t(u, \varphi, F)$ for $\varphi$ a vector of the row side and $F$ a vector of the column side. Let $e_V$ be a map of the column side and $s$ a map on $E_E$.

**Definition 4.2.3 (Period identity).** A *period datum* for $X$ is a tuple $d = (V, a, U, \zeta)$ of a linear map $V$ of $E_E$, complex numbers $a_u$, square matrices $U_u$ and complex numbers $\zeta_u(t)$. It is *unitary* if $V$ preserves $E_{E,l}$ and the norm, each $U_u$ preserves the norm, each $\zeta_u(t) \neq 0$, $\zeta_u(\mu_0) = 1$, and $v(w, k) = 0$ whenever $\zeta_u(\mu(w))$ is the image of $k$. It satisfies the *identity* if for all $u, t, \varphi, F$:

$$\zeta_u(t)\, \iota\bigl(P_t(u, \varphi, F)\bigr) = a_u \bigl\langle s\bigl(V(\Theta_t(j_R(t)(e_V(t)\, F)))\bigr),\; P_u(U_u \cdot c(\iota \circ \varphi)) \bigr\rangle .$$

Here $\iota$ is the embedding of the field of coefficients in $\mathbb{C}$, $j_R(t)$ is the row map, $c$ is the compact part and $P_u$ is the projection to the vectors of $u$. The space $X$ satisfies the *period identity* $\mathrm{MI}^*_2$ if there is a unitary period datum with the identity and with $a_u \neq 0$ for all $u$.

So the period identity says that each period of $X$ equals, up to a nonzero scalar and a unitary change of coordinates, an inner product of a theta vector with a vector of the row side. Each bundle condition $b$ has a package with a coefficient space $X_b$, a map $e_V$ and a map $s$. We say that $b$ satisfies the period identity if $X_b$ does.

**Definition 4.2.4 (Multiplicity row).** A parameter set $p$ satisfies the *multiplicity row* if it is linked at the row statement $(S, \Lambda) \mapsto \mathrm{Row}(S, \Lambda, \mathrm{EvW}(\mathrm{MI}^*_2))$.

We need three facts on rows. (i) If $\mathrm{RowE}(Q, \Lambda, E)$ holds with $E(\kappa, D, O, c, b) = R(b)$, then $\mathrm{Row}(Q, \Lambda, \mathrm{AtAll}(R))$ holds, with the same $E$. (ii) $\mathrm{AtAll}(R)$ implies $\mathrm{EvW}(R)$. (iii) A row in the good bundles of $p$ gives a linked row at $p$. Eventual rows are also closed under conjunction and under pointwise implication. These facts are lemmas of the calculus of rows, and we use them as given.

**Theorem 4.2.5 (Period identity from point conditions).** Assume thirteen of the published statements of [the open parameter statements](/entry/open0-of-unitary-group-hypotheses/): the finiteness theorem, the rapid decay of cusp forms, the discrete series cover, the Harish-Chandra modules, the Casselman-Wallach theorem, the unramified Howe duality, the Weil representation, the Weil-Siegel formula, the Siegel-Weil convergence, the doubling method, the unramified doubling, the classification of discrete series and strong approximation. Assume the diagonal row: the row of the data whose scale has bounded gamma factors and rank $\mu$ at each word. Let $h_L$ be a recursion datum and $p$ a parameter set. Assume that each witness point of the scale of $p$ has a real datum. If the eventual row of the point conditions holds in the good bundles of $p$, then the eventual row of the period identity holds there:

$$\mathrm{RowE}(Q'_p, \Lambda_p, \mathrm{BPC}) \implies \mathrm{RowE}(Q'_p, \Lambda_p, \mathrm{MI}^*_2).$$

Lean: `GlobalTheory.Fam.miStar_row_alt_alt` (also `GlobalTheory.T.main_theorem_published_results_final_alt_alt`, a second name).

The point conditions $\mathrm{BPC}(b)$ of a bundle condition are ten conditions: a realisation join, a decomposition point, frames, an extension of the realisation, a real datum, primitive rows with separated types, finiteness, two gap conditions, and $1 \leq r_S$ for the integer $r_S$ of the datum.

*Proof.* Let $b$ be a bundle condition with the point conditions at a linked bundle. The linkage gives a witness point $q$, a bundle condition $b'$ at $q$, a witness $w$ and an equality of the data of $b$ and of $b'$. [The Theorem on bundle witnesses](/entry/true-pack-of-bundle-witness/) gives that the package of $b'$ is a true package; it uses the real datum at $q$. We transport this along the equality to $b$. So the row of true packages holds. From the diagonal row and the row of true packages, a result of another chapter gives the row of the condition $\mathrm{PuNZ}$ of the next section. Now take the conjunction of the three rows. At each bundle, the point condition $1 \leq r_S$, the true package and $\mathrm{PuNZ}$ are the hypotheses of [the Theorem of the next section](/entry/main-theorem-from-published-results-alt-alt-alt-alt-alt/), which gives the period identity. $\square$

**Theorem 4.2.6 (Period identity at good linked bundles).** Under the thirteen published statements and the diagonal row, for each $h_L$ and each parameter set $p$ whose witness points have real data, the eventual row $\mathrm{RowE}(Q'_p, \Lambda_p, \mathrm{MI}^*_2)$ holds.

Lean: `GlobalTheory.miStarRowClosing_alt_alt` (also `GlobalTheory.T.main_theorem_published_inputs_variant_alt_alt`, a second name).

*Proof.* The discrete series cover, the Harish-Chandra modules, the Casselman-Wallach theorem, the finiteness theorem and the rapid decay of cusp forms give the eventual row of the point conditions at $p$, by a result of another chapter. Then apply [the Theorem on point conditions](/entry/fam-mi-star-row-alt-alt/). $\square$

**Theorem 4.2.7 (Multiplicity rows).** Assume the thirteen published statements above and a second form of the Siegel-Weil convergence for unitary groups. Then for each recursion datum $h_L$, each extension choice $N$, each $S$-extension $S$ and each geometry $\Gamma$, the parameter set $p = p(N, S, \Gamma)$ is linked at $\mathrm{Row}(\cdot, \cdot, \mathrm{AtAll}(\mathrm{MI}^*_2))$ and satisfies the multiplicity row.

Lean: `GlobalTheory.miStarRow_alt_alt` (also `GlobalTheory.T.main_theorem_published_inputs_third_alt_alt`, a second name).

*Proof.* The second form of the Siegel-Weil convergence gives the diagonal row, by [the Theorem on the diagonal row](/entry/diagonal-row-of-siegel-weil-unitary/). Each witness point of the scale of $p$ carries a real datum as one of its components. So [the Theorem on good linked bundles](/entry/mi-star-row-closing-alt-alt/) applies and gives $\mathrm{RowE}(Q'_p, \Lambda_p, \mathrm{MI}^*_2)$. By fact (i) this gives $\mathrm{Row}(Q'_p, \Lambda_p, \mathrm{AtAll}(\mathrm{MI}^*_2))$, and fact (iii) makes it a linked row. By fact (ii) the same row holds with $\mathrm{EvW}$ in place of $\mathrm{AtAll}$, and fact (iii) gives the multiplicity row. $\square$

**Remark 4.2.8 (Formalization).** The theorems are at [MainTheoremPublishedInputsThird.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedInputsThird.lean#L22), [MainTheoremPublishedInputsVariant.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedInputsVariant.lean#L21) and [MainTheoremPublishedResultsFinal.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedResultsFinal.lean#L24); each has a second name a few lines below that only passes its hypotheses on. The names "main theorem", "published inputs", "third", "variant", "closing" and "final" do not describe the statements. The second conclusion of the multiplicity rows follows from the first by `evW_of_atAll`, so it is the weaker of the two. The fourteenth hypothesis is `HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent`, a different statement from `GlobalTheory.Published.SiegelWeilUnitaryConvergent` with the same last name; only it is used to build the diagonal row. The diagonal row is `RowDiag (fun D L C' => IsScaleWithBoundedGamma D L C' ∧ ∀ u, RankMu D u)`, which we did not unfold; we also did not unfold `Closed`, `W3`, `IsSel`, `BundleLinkage` or the package maps `eV` and `sEE`. Facts (i) to (iii) are `RowE.row`, `evW_of_atAll` and `LinkedAt.of_row`, which we did not open. The rows of point conditions and of `PuNZ` come from `point_lines_of_cusp_rapid_decay` and `puNZ_of_truePack`, which we did not open. The transport in the first proof is a small lemma `key` on dependent pairs; it is needed because the linkage gives the equality of $b$ and $b'$ as an equality of triples $(D, O, b)$.
