---
title: The service row from Artin reciprocity
decls:
  - GlobalTheory.Svd.servH_row
  - GlobalTheory.T.bundle_bothParts_of_standardKernel_and_six_hypotheses
  - GlobalTheory.Svd.servH_row_of_artin
  - GlobalTheory.T.bundle_bothParts_of_standardKernel_of_globalArtinReciprocity
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The service row from Artin reciprocity

This section proves the *service row*. For a family of bundles over constructed points, the service row says two things: the family class is closed under the twisted unitary row condition, and every selected bundle satisfies the kernel condition for its kernel entry. The first part comes from the local models of Section 5. The second part comes from [the kernel row of a standard tie](/entry/row-at-of-std-tie/). We prove the service row first from six hypotheses, and then from global Artin reciprocity alone. The result is used in [the service row of the unitary hypotheses](/entry/serv-h-row-link-r-alt/) of Volume 15, and through it in the step [the unitary hypotheses](/step/hyps-alt-def/) of [the written proof](/proof/unitary-hypotheses/).

### Rows over constructed points

A *parameter* $\kappa$ fixes a small number $\varepsilon$ and constants $C$, $c_D$, $c_h$, $C_5$, $c_6$, $C_b$. It is *positive* if $C_5, c_6, C_b > 0$. A context $\mathcal{K}$ *belongs to* $\kappa$ if it has the same constants and the good character conditions hold for them. A property of parameters holds *eventually* if there is $\varepsilon_0 > 0$ such that for every $\varepsilon \le \varepsilon_0$ with $\varepsilon < 1/52$, every $C_8 \ge 1$ and all $C_5, c_6, C_b$, there is a threshold for the constants $C$, and for each $C$ beyond it there are $c_1$ and then $c_2$ such that the property holds for all $c_D \ge c_1$ and $c_h \ge c_2$. A property $E(\kappa, \mathcal{K})$ holds *eventually at large scale* if, eventually in $\kappa$, for every positive $\kappa$ there is $x_0$ such that $E(\kappa, \mathcal{K})$ holds for every context $\mathcal{K}$ of $\kappa$ with scale $x \ge x_0$.

Let $Q$ be a *slot*, that is, a property of cores of constructed points. Let $\mathrm{Bd}$ be a type of bundles: for a datum $D$, an object $O$ over $D$ and a real number $c$, it gives a set $\mathrm{Bd}(D, O, c)$. Let $\mathrm{Lk}$ be a *linkage*, a relation between constructed points $\beta$, numbers $c$ and bundles $b \in \mathrm{Bd}(\beta.D, \beta.O, c)$.

**Definition 5.6.1 (Row condition).** Let $E$ be a property of bundles that depends on a parameter. The *row condition* for $E$ says: eventually at large scale, for every constructed point $\beta$ in $\mathcal{K}$ whose core satisfies $Q$, every $c$ and every bundle $b$ linked to $\beta$ and $c$, the property $E(\kappa, \beta.D, \beta.O, c, b)$ holds.

**Definition 5.6.2 (Row).** Let $H$ be a property of pairs $(\mathcal{A}, \sigma)$, where $\mathcal{A}$ is a family class and $\sigma$ is a raw selection of bundles for $\mathcal{A}$. We say that $H$ *holds in a row* for $(Q, \mathrm{Lk})$ if there is a property $E$ with the row condition such that $H(\mathcal{A}, \sigma)$ holds for every selection $\sigma$ along $E$. A selection is *along* $E$ if for every family in $\mathcal{A}$ there is a parameter $\kappa$ linked to the family such that every selected bundle is built from a point with $Q$ and satisfies $E(\kappa, \cdot)$.

Two rows combine: if $H$ and $H'$ hold in a row, then so does $H \wedge H'$. For the proof one takes the conjunction of the two properties $E$ and $E'$.

**Definition 5.6.3 (Service condition).** Let $\mathrm{ker}$ assign to each bundle $b \in \mathrm{Bd}(D, O, c)$ a tied kernel entry for the extra data of $O$. The *service condition* for $(\mathcal{A}, \sigma)$ is the conjunction of:
1. the family class $\mathcal{A}$ is closed under the twisted unitary row condition;
2. every selected bundle $b \in \mathrm{Bd}(D, O, c)$ satisfies the kernel condition for the extra data of $O$ and the entry of $\mathrm{ker}(b)$.

### Six hypotheses

The service row uses six statements, each about all CM data.
1. *Algebraic torsion.* The Taylor coefficients at torsion points of the curves of the development are algebraic.
2. *Genus one models.* Every lattice of the development has a genus one model.
3. *Curve dictionary.* The dictionary between lattices and curves holds.
4. *Inert integrality.* The integrality statement at inert primes holds.
5. *Inert admissibility.* The inert admissibility hypothesis of Section 5 holds.
6. *Curve existence.* The curve existence hypothesis of Section 2 holds.

**Theorem 5.6.4 (Service row from six hypotheses).** Assume the six hypotheses. Let $Q$ be a slot, $\mathrm{Lk}$ a linkage and $\mathrm{ker}$ a kernel assignment. Assume that every core with $Q$ is at a position with a part, and that the standard tie of $\mathrm{ker}(b)$ satisfies the row condition. Then the service condition holds in a row for $(Q, \mathrm{Lk})$.

Lean: `GlobalTheory.Svd.servH_row` (also `GlobalTheory.T.bundle_bothParts_of_standardKernel_and_six_hypotheses`)

*Proof.* Let $\beta$ be a constructed point whose core satisfies $Q$. By hypothesis its core is at a position with a part. By [the theorem on local models at a constructed point](/entry/models-at-bpt/), which uses hypotheses 5 and 6, the object $\beta.O$ satisfies the local model condition. This holds for every $\beta$, every parameter and every context. So the local model condition satisfies the row condition, with no largeness needed.

[The theorem on the twisted unitary row](/entry/row-tw-u/) turns the row condition for local models into part 1 of the service condition, in a row. [The kernel row of a standard tie](/entry/row-at-of-std-tie/) uses hypotheses 1 to 4 and the row condition for the standard tie, and gives part 2 of the service condition, in a row. The two rows combine. $\square$

### Global Artin reciprocity

Let $E$ be a number field and $\Omega$ an algebraic closure of $E$. Write $\mathbb{I}_E$ for the ideles of $E$ and $G^{\mathrm{ab}}_E$ for the Galois group of the maximal abelian extension of $E$ in $\Omega$. *Global Artin reciprocity* says that for every such $E$ and $\Omega$ there is a homomorphism $\mathrm{art} : \mathbb{I}_E \to G^{\mathrm{ab}}_E$ with these properties:
1. it is an open quotient map;
2. its kernel is the closure of $E^\times$ times the identity component at the archimedean places;
3. at each finite place $v$ it maps the units of $E_v$ onto the inertia group of $v$;
4. it maps a uniformizer at an unramified place $v$ to an inverse Frobenius element at $v$;
5. the closure of the image of $E_v^\times$ is the decomposition group of $v$.

See [global class field theory](/learn/class-field-theory/#global-class-field-theory) and [[Artin reciprocity|7938EKMMVR]].

The link to the six hypotheses is the existence of good models of CM curves. The statement CM2 says: let $d$ be squarefree with $d \equiv 3 \pmod 4$, and let $\Lambda$ be a lattice with $\omega \Lambda \subseteq \Lambda$, where $\omega = (1 + \sqrt{-d})/2$. Let $l \ge 5$ be a prime with $l \nmid d$, and let $\iota : \mathbb{C} \to \mathbb{C}_l$ be a field isomorphism. Then there are $g_2, g_3$ in the closure of the field generated by the roots of unity of order prime to $l$, with $|g_2|, |g_3| \le 1$ and $|g_2^3 - 27 g_3^2| = 1$, and $\lambda \ne 0$ with
$$g_2 = \lambda^4\, \iota(g_2(\Lambda)), \qquad g_3 = \lambda^6\, \iota(g_3(\Lambda)).$$
So the curve of $\Lambda$ has good reduction at $l$ over the maximal unramified extension. See [complex multiplication](/learn/elliptic-curves/#complex-multiplication) and [reduction and minimal models](/learn/elliptic-curves/#reduction-and-minimal-models).

**Theorem 5.6.5 (Service row from Artin reciprocity).** Assume global Artin reciprocity. Let $Q$, $\mathrm{Lk}$ and $\mathrm{ker}$ be as in the previous theorem, such that every core with $Q$ is at a position with a part, and the standard tie of $\mathrm{ker}(b)$ satisfies the row condition. Then the service condition holds in a row for $(Q, \mathrm{Lk})$.

Lean: `GlobalTheory.Svd.servH_row_of_artin` (also `GlobalTheory.T.bundle_bothParts_of_standardKernel_of_globalArtinReciprocity`)

*Proof.* [Good models from Artin reciprocity](/entry/cm-good-model-of-global-artin-reciprocity/) gives CM2. From CM2 we get the six hypotheses:
1. [algebraic torsion and lattice models](/entry/torsion-taylor-algebraic-lattice-exists-of-cm/) give hypotheses 1, 2 and 3;
2. a theorem on the condition of complex multiplication gives hypothesis 4;
3. [the inert theta admissibility theorem](/entry/inert-theta-admissibility-of-complex-multiplication/) gives hypothesis 5;
4. [the formal isomorphism at a prime of good reduction](/entry/exists-genus-one-formal-iso-of-unramified-good-reduction/) gives hypothesis 6.

The service row from six hypotheses now gives the result. $\square$

**Remark 5.6.6 (Formalization).** Several facts about the Lean code:
1. The names `GlobalTheory.T.bundle_bothParts_of_standardKernel_and_six_hypotheses` and `GlobalTheory.T.bundle_bothParts_of_standardKernel_of_globalArtinReciprocity` are second names, each proved by the tactic `first | exact @… | …` under `maxHeartbeats 1000000`. The file name `BundleBothPartsOfStandardKernelOfGlobalArtinReciStatement.lean` is truncated.
2. Global Artin reciprocity is used only to obtain CM2, by `GlobalTheory.Corev.CmTwoClosing.cmGoodModel_of_globalArtinReciprocity` (BundleBothPartsOfStandardKernelOfGlobalArtinReci.lean:21). The other five inputs are all derived from CM2. The statement `GlobalArtinReciprocity` is in ExistsUniqueHcharOfFiniteOrder.lean:70, and CM2 is in Formalism/LocalToGlobal/TorsionIntegrality/CMGoodModels/Statement.lean:45.
3. The hypothesis "inert integrality" comes from `GlobalTheory.intInert_of_complexMultiplication_condition`, which is not in the chapter outline, so it has no entry link.
4. The service condition is `ServH` (HasPartAnd.lean:45). Its first part, `Closed 𝒜 RowTwU`, does not depend on the selection or on the kernel assignment. The rows are `RowE` and `Row` (ValidForConstructedPointClassesEventuallyWorking.lean:261 and :268), and the eventual quantifier is `ParEv` (same file, line 122).
5. In `GlobalTheory.Svd.servH_row` the six hypotheses split cleanly: the first four go only to the kernel row `GlobalTheory.Pdv.rowAt_of_stdTie`, and the last two go only to the local models (BundleBothPartsOfStandardKernelAndSixHypotheses.lean:21). The row for local models is built with `RowE.of_all`, so it needs no largeness.
