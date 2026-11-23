---
title: Lattice inclusions at the short and coarse weight bounds
decls:
  - Formalism.CohomologicalDescent.ShortWeightBounds.inclusion_w_of_shape_w
  - Formalism.CohomologicalDescent.ShortWeightBounds.inclusion_w_real_holds
  - Formalism.CohomologicalDescent.Down.inclusion_w_real_holds
  - Formalism.CohomologicalDescent.Down7.inclusion_w_seven_real_holds
  - Formalism.CohomologicalDescent.Top.inclusion_w_seven_real_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lattice inclusions at the short and coarse weight bounds

This section specializes the [weight theorem at the top](/entry/theorem-w-top-short-bound-holds/) to the weights that occur in the proof. The weights come with a record of numerical parameters and a weight datum. From these we read off the window of each factor, the exponents of the integral inclusions and a depth budget. The result is the lattice inclusion: for every prime $l$ above a threshold, $l^{J}$ moves the localized forms with values in the dual Weyl modules into the forms with values in the Weyl lattices, first with a short exponent $J_W(l)$ and then with a coarse exponent $J^{c}_W(l) \geq J_W(l)$. The coarse form is the one used by the [inclusion of models](/entry/l-incl-of-models/): its exponent at $l$ is the coarse bound when $l > l_J$, $l$ is not excluded and $l$ is not special, and the sum $\sum_\tau \mathrm{ex}_\tau(l)$ otherwise.

**Definition 4.4.1 (Hida setting).** Let $\iota$ be a finite set, $N \in \mathbb{N}$ and $\lambda_\tau : \mathbb{N} \to \mathbb{N}$ for $\tau \in \iota$. A *Hida setting* for $(\iota, N, \lambda)$ consists of a Noetherian local domain $O$ of characteristic zero, an $O$-algebra $A$, a group $G$ with subgroups $\Gamma$ and $K$, a homomorphism of monoids $j_K : K \to A$, an action of $A$ on $V = \bigotimes_\tau \nabla_O(\lambda_\tau|_N)$, a commutative $O$-algebra $T$ acting on the forms $\mathcal{F}(V)$, and a multiplicative set $S \subseteq T$. For a prime $l$ and $J \in \mathbb{N}$ we say that the setting has an *inclusion of exponent $J$ at $l$* if the inclusion at the top holds with exponent $J$ (Section 3). Let $J_{\min}(l)$ be the least such $J$ (with $J_{\min}(l) = 0$ if there is none).

The forms are vector-valued forms of level $\Gamma$ and type $j_K$. The number $J_{\min}(l)$ measures how far the lattice of forms with values in $\bigotimes \nabla$ is from the lattice of forms with values in $\bigotimes \Delta$ at $l$.

**Definition 4.4.2 (Parameters and weight data).** We fix a record $P$ of parameters with two conditions, the hypotheses and the largeness of $P$. We use from it: a rank $N_r$, integers $k \geq 1$ and $t$, a real height $h \geq 1$ with integer part $h_0 = \lfloor h \rfloor$, and a real threshold $l_J$. Put $k_c = k - 1$ and $\kappa_l = \lfloor h/(l-1) \rfloor$. A *weight datum* $W$ consists of weights $\lambda_\tau$, a subset $T_2 \subseteq \iota$ of *thick* indices, integers $j_\tau, q_\tau$, integer windows $[x_{-,\tau}, x_{+,\tau}]$, real centres, a partner map $\tau \mapsto \tau'_l$ with a reflection flag for each $l$, and a finite set of special primes. With $U_\tau(a) = U_{N_r}(\lambda_\tau, a)$, the datum is *admissible* for $P$ if, among other conditions: $\lambda_\tau$ is non-increasing on $[0, N_r)$; $k_c + j_\tau + t + q_\tau = N_r$; $\lambda_\tau$ is constant on $[k_c + j_\tau, k_c + j_\tau + t)$; $x_{-,\tau} \leq U_\tau(a) \leq x_{+,\tau}$ for $a < k_c$; and the window of a thick index lies below $h$. For a prime $l$ put:

1. $\mathrm{ex}_\tau(l)$, the least $e$ such that $m\, l^e \nabla_{\mathbb{Z}}(\lambda_\tau|_{N_r}) \subseteq \Delta_{\mathbb{Z}}(\lambda_\tau|_{N_r})$ for some $m$ prime to $l$, and $e_{\mathrm{cl},\tau}(l)$, the same number for $\lambda_\tau|_{k_c}$;
2. $m_\tau(l)$, the number of shifted entries $u \in \{U_\tau(a) : a < N_r\}$ outside the block $[b_\tau, b_\tau + t - 1]$ that are congruent modulo $l$ to some point of $[b_\tau - \kappa_l, b_\tau + t - 1 + \kappa_l]$, where $b_\tau = U_\tau(k_c + j_\tau + t - 1)$; and $m^F_\tau(l)$, the same count for the partner $\tau'_l$, with the entries $u$ replaced by $h_0 - u$ when the flag is set;
3. the *depth budget* $i_\tau(l) = \bigl\lfloor q_\tau h + (l\, m^F_\tau(l) + m_\tau(l))(t + 2\kappa_l) \bigr\rfloor$.

The *short weight bound* and the *coarse weight bound* are
$$J_W(l) = \sum_{\tau \in \iota} c_\tau(l), \qquad J^{c}_W(l) = \sum_{\tau \in \iota} c^{c}_\tau(l),$$
where $c_\tau(l) = c^{c}_\tau(l) = \mathrm{ex}_\tau(l)$ for $\tau \notin T_2$, and for $\tau \in T_2$,
$$\begin{aligned} c_\tau(l) &= \min\bigl(\mathrm{ex}_\tau(l), \lfloor c^{\mathrm{sh}}_l \rfloor\bigr), \\ c^{c}_\tau(l) &= \min\bigl(\mathrm{ex}_\tau(l), \lfloor c^{\mathrm{sh}}_l + 6(q_\tau + 2 j_\tau) \rfloor\bigr), \end{aligned}$$
with $c^{\mathrm{sh}}_l = c^{\mathrm{sh}}_l(k_c, j_\tau, t, q_\tau, h_0, e_{\mathrm{cl},\tau}(l), N_r; x_{-,\tau}, x_{+,\tau}, U_\tau(k_c + j_\tau); i_\tau(l))$ the short constant of Section 3.

The count $m_\tau(l)$ is the number of rows outside the block whose shifted entry is linked to the block modulo $l$ with a margin $\kappa_l$. [Section 4.5.8](/entry/weight-inputs-of-linkage-holds/) proves that the depth of every relevant highest weight is at most $i_\tau(l)$.

**Definition 4.4.3 (Weight inputs at $l$).** A Hida setting has the *weight inputs at $l$* if there are $\varpi \in O$, $n_0 \in \mathbb{N}$, elements $e_\tau(w) \in A$, $A$-modules $L_\mu$ and weights $\mathrm{hw}(\mu, \tau)$ such that: $O/lO$ is finite and $l \mid \varpi^{n_0}$; $A$ preserves the mixed lattices and $e_\tau(w)$ acts by the component of row weight $w$ on the factor $\tau$; the Hecke conditions hold; every simple subquotient of $V / \varpi V$ is some $L_\mu$, and $e_\tau(\mathrm{hw}(\mu, \tau)) \neq 0$ on $L_\mu$; and the depth bound holds with the budget $i_\tau(l)$ for $\tau \in T_2$.

These are inputs 4 to 6 of the inputs at the top, together with the finiteness of $O/lO$ and the divisibility $l \mid \varpi^{n_0}$. The following two lemmas give the other inputs.

**Lemma 4.4.4 (Window shape of thick indices).** Let $P$ satisfy the hypotheses and be large, and let $W$ be admissible for $P$. For every $\tau \in T_2$ the data $(N_r, k_c, j_\tau, t, q_\tau, h_0, \lambda_\tau, x_{-,\tau}, x_{+,\tau})$ have window shape.

Lean: `Formalism.CohomologicalDescent.ShortWeightBounds.shape_w_real_holds`.

*Proof.* The conditions on $N_r$, the monotonicity, the block, the position of the first $k_c$ entries and $x_- \leq x_+$ are parts of admissibility. The bound on the spread and the conditions $U_\tau(a) < x_{-,\tau}$ for the rows below the window follow from the thickness of $\tau$ and the size conditions on $P$. The bound $x_{+,\tau} - U_\tau(k_c + j_\tau) \leq h_0$ follows from $x_{+,\tau} \leq h_0$ (an integer at most $h$) and $U_\tau(k_c + j_\tau) \geq 0$. $\square$

**Lemma 4.4.5 (Inputs at the top from weight inputs).** Let $P$ satisfy the hypotheses and be large, let $W$ be admissible for $P$, and let $l > l_J$ be a prime that is not a unit in $O$. If the setting has the weight inputs at $l$, then the inputs at the top hold for the data $(l, N_r, k_c, t, h_0, \lambda, T_2, j, q, x_\pm, e_{\mathrm{cl}}(l), \mathrm{ex}(l), i(l))$.

Lean: `Formalism.CohomologicalDescent.ShortWeightBounds.top_inputs_of_shape_w` (also `Formalism.CohomologicalDescent.ShortWeightBounds.top_inputs_real_holds`).

*Proof.* Let $m$ be an integer prime to $l$. There are integers $a, b$ with $a l + b m = 1$. If $m$ were not a unit of the local ring $O$, then $l$ and $m$ would both lie in the maximal ideal, and so would $1$. Hence every integer prime to $l$ is a unit in $O$. For $l > l_J$ the size conditions on $P$ give $h + N_r < l^2$, so $h_0 < l^2$; the hypotheses give $t \geq 1$. The window shape is the previous lemma. The least exponent $\mathrm{ex}_\tau(l)$ is attained, so the integral inclusion holds with it. The integral inclusion for $\lambda_\tau|_{k_c}$ with exponent $e_{\mathrm{cl},\tau}(l)$ gives $\mathrm{Exp}_l(\lambda_\tau|_{k_c}, \mu) \leq e_{\mathrm{cl},\tau}(l)$ for every $\mu$. The other inputs are the weight inputs. $\square$

**Theorem 4.4.6 (Inclusion at the short weight bound, conditional form).** Assume Lemma D in its graded form. Let $P$ satisfy the hypotheses and be large, let $W$ be admissible for $P$, and let $X$ be a Hida setting for $(\iota, N_r, \lambda)$. Let $l > l_J$ be a prime that is not a unit in $O$, and assume that $X$ has the weight inputs at $l$. Then $X$ has an inclusion of exponent $J_W(l)$ at $l$, and $J_{\min}(l) \leq J_W(l)$.

Lean: `Formalism.CohomologicalDescent.ShortWeightBounds.inclusion_w_of_shape_w` (also `Formalism.CohomologicalDescent.ShortWeightBounds.inclusion_w_real_holds`, the form with the window lemma filled in).

*Proof.* By [Lemma D for the last block](/entry/formalism-cohomological-descent-ld-last-graded-of-graded-alone/), the graded form of Lemma D gives its last block form. The previous lemma gives the inputs at the top. The [weight theorem at the top with the short constant](/entry/theorem-w-top-short-bound-holds/), with $N' = N_r$, gives the inclusion with exponent $J_W(l)$ and the bound on the least exponent. $\square$

**Theorem 4.4.7 (Inclusion at the short weight bound).** Under the hypotheses of the conditional form without the assumption on Lemma D, $X$ has an inclusion of exponent $J_W(l)$ at $l$, and $J_{\min}(l) \leq J_W(l)$.

Lean: `Formalism.CohomologicalDescent.Down.inclusion_w_real_holds`.

*Proof.* This is the conditional form applied to [Lemma D](/entry/h-g/), which is proved in Section 2. $\square$

**Theorem 4.4.8 (Inclusion at the coarse weight bound).** Let $P$ satisfy the hypotheses and be large, let $W$ be admissible for $P$, and let $X$ be a Hida setting for $(\iota, N_r, \lambda)$. Let $l > l_J$ be a prime that is not a unit in $O$, and assume that $X$ has the weight inputs at $l$. Then $X$ has an inclusion of exponent $J^{c}_W(l)$ at $l$, and $J_{\min}(l) \leq J^{c}_W(l)$.

Lean: `Formalism.CohomologicalDescent.Down7.inclusion_w_seven_real_holds` (also `Formalism.CohomologicalDescent.Top.inclusion_w_seven_real_holds`, a second name).

*Proof.* For $\tau \in T_2$ we have $c^{\mathrm{sh}}_l \leq c^{\mathrm{sh}}_l + 6(q_\tau + 2j_\tau)$, so $c_\tau(l) \leq c^{c}_\tau(l)$, since the floor and $\min(\mathrm{ex}_\tau(l), \cdot)$ are monotone. For $\tau \notin T_2$ the two terms are equal. Hence $J_W(l) \leq J^{c}_W(l)$. By the [inclusion at the short weight bound](/entry/down-inclusion-w-real-holds/), $X$ has an inclusion of exponent $J_W(l)$. If $l^{J} y$ is the image of a form with values in the Weyl lattices, so is $l^{J'} y = l^{J' - J}(l^J y)$ for $J' \geq J$. This gives the inclusion of exponent $J^{c}_W(l)$, and $J_{\min}(l) \leq J_W(l) \leq J^{c}_W(l)$. $\square$

**Remark 4.4.9 (Formalization).** The parameter record $P$, its hypotheses, its largeness and the full admissibility condition were not unfolded; the text lists only the parts that the proofs above use. The window lemma uses three lemmas on thick indices that were opened only at the level of their names and uses. There are two predicates named `InclWReal`: the one in [StatementDown.lean](lean:Formalism/PieriBlockIdeals/StatementDown.lean#L204) has no hypothesis of Lemma D, and the one in [LatticeInclusionRealSettingAlt.lean](lean:Formalism/PieriBlockIdeals/LatticeInclusionRealSettingAlt.lean#L318) has it. The predicate of the coarse inclusion is defined three times: LatticeInclusionRealSettingAlt.lean line 455 (with Lemma D as a hypothesis), HidaLatticeInclusionAtCoarseWeightBound.lean line 12 and StatementTop.lean line 13 (both without it, and equal by definition). A further theorem `ShortWeightBounds.inclusion_w_seven_real_holds` (WeightBounds.lean, line 674) proves the conditional form of the coarse inclusion through a coarse top theorem; it is not on the path of this chapter. The private lemma `Incl_mono` (CorollaryOfParamsSevenLinkage.lean, line 33) repeats the monotonicity `top_inclusion_monotone_holds` (DepthNonnegative.lean, line 907). The file of the second name of the coarse inclusion also contains `prime_count_bound_rs`, a second name of `prime_count_bound` (CorollaryOfParamsSevenLinkageAlt.lean, line 7). The proof that Lemma D holds is named `hG` (CorollaryOfParamsLinkage.lean, line 9); the name does not describe it.
