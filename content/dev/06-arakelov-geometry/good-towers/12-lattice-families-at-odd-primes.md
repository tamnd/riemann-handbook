---
title: Lattice families at odd primes
decls:
  - GlobalTheory.T.family_pos_of_hodge_tate_inputs
  - GlobalTheory.CompanionTheory.Ar.Num.FamEx.familyExistsPos_holds
  - GlobalTheory.T.ordinary_curve_hodge_prime
  - GlobalTheory.CompanionTheory.Ar.Num.FamEx.TestPt.testFacts
  - GlobalTheory.T.arith_variety_model_hodge_relay
  - GlobalTheory.CompanionTheory.Relay.arith_variety_model_hodge_relay
  - GlobalTheory.T.ordinary_curve_model_relay
  - GlobalTheory.CompanionTheory.Relay.ordinary_curve_model_relay
  - GlobalTheory.T.arith_variety_model_prime_degree
  - GlobalTheory.CompanionTheory.Ar.Num.FamEx.Seq.seq_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Lattice families at odd primes

The [Chern numbers of the Hodge flag](/entry/model-on-hodge-of-family-pos/) at a prime $p$ are computed from a family of lattices on the charts of the Hodge component, with the Frobenius action on the labels. This section proves that such a family exists at every odd prime $p$ at which the Hodge component is Hodge-Tate free and $p \nmid d_E$. The proof builds the lattices from the $p$-torsion of the semi-abelian scheme, checks the base conditions over the ring of the chart, and checks the test facts at every test point. The test facts come from the tightness of the test orders and from the test group points of [Theorem 7.9.8](/entry/tight-hopf-order-test/) and [Theorem 7.9.9](/entry/test-group-point-exists/). The result is used in [the good tower theorem](/entry/good-tower-and-volume/), where the last two inputs are proved and the first three stay as hypotheses.

We assume five published results, as in [Theorem 7.9.9](/entry/test-group-point-exists/): the Hodge-Tate statement of Fargues, the statement on quotients by finite flat subgroups, Zarhin's statement, the Hodge-Tate datum statement and the ordinary curve statement. Their sources are given at the end of the chapter.

### Lattice data

Let $\Omega$ be a field, $F$ a finite field with $|F| = f$, $n \ge 1$, and $\Sigma$ a finite set of labels with ranks $r(\tau)$ and $s(\tau)$. Let $R \subset \Omega$ be a subring and $w \in \Omega$. The standard lattice $\mathrm{std}$ of a space $\Omega^m$ is $R^m$. For a lattice $L$ let $wL$ and $w^{-1}L$ be its multiples and let $L^{\vee}$ be its dual for the dot product.

**Definition 8.12.1 (Base conditions).** As in [the Chern-Weil chapter](/entry/arakelov-geometry/chern-weil/#eigenspace-splitting-on-normal-models), a Lie lattice datum $\mathcal{D}$ consists of a lattice $M$ of functions $F^n \to \Omega$, and for each label $\tau$ lattices $\mathrm{Lie}_\tau, W_\tau \subset \Omega^{r(\tau)}$ and $\omega_\tau, \omega^{\mathrm{HT}}_\tau \subset \Omega^{s(\tau)}$, and three lattices of pairs
$$
\Gamma_\tau \subset \Omega^{r(\tau)} \times \Omega^{n}, \quad \Delta_\tau \subset \Omega^{n} \times \Omega^{s(\tau)}, \quad \Theta_\tau \subset \Omega^{F^n} \times \Omega^{r(\tau)}.
$$
The datum satisfies the base conditions over $R$ at $(p, w)$ if these hold.

1. $M$ is locally free of rank $f^n$, $p^m\,\mathrm{std} \subset M \subset \mathrm{std}$ for some $m$, and $1 \in M$.
2. $\mathrm{Lie}_\tau$, $W_\tau$, $\omega_\tau$, $\omega^{\mathrm{HT}}_\tau$ are locally free of ranks $r(\tau)$, $r(\tau)$, $s(\tau)$, $s(\tau)$, with $\mathrm{Lie}_\tau \subset W_\tau \subset w^{-1}\mathrm{Lie}_\tau$ and $\omega^{\mathrm{HT}}_\tau \subset \omega_\tau \subset w^{-1}\omega^{\mathrm{HT}}_\tau$.
3. $\Gamma_\tau$, $\Delta_\tau$, $\Theta_\tau$ are $R$-modules.
4. $\Gamma_\tau$ is the graph of a map from $w^{-1}W_\tau$ to $\Omega^n / \mathrm{std}$: its first projection is $w^{-1}W_\tau$, its fibre over $0$ is $\mathrm{std}$, and $(a, 0) \in \Gamma_\tau$ if and only if $a \in W_\tau$.
5. $\Delta_\tau$ is the graph of a map from $w^{-1}\mathrm{std}$ to $\Omega^{s(\tau)}/\omega^{\mathrm{HT}}_\tau$ with image $w^{-1}\omega^{\mathrm{HT}}_\tau$, and its kernel is the image of $\Gamma_\tau$.
6. The first projection of $\Theta_\tau$ is the set of $g \in M$ with $g(0) = 0$, its second projection is $\mathrm{Lie}_\tau^{\vee}$, and its fibre over $0$ is $p\,\mathrm{Lie}_\tau^{\vee}$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.LieLatticeData.Base`.

So $\Gamma_\tau$ and $\Delta_\tau$ are graphs of maps between quotients of lattices, as for the two steps of a short exact sequence, and $\Theta_\tau$ pairs the functions in $M$ with the dual Lie lattice.

For a character $\chi \colon F \to \Omega$ let $a_\chi \subset \Omega^n$ be the pull back of $M + p\,\mathrm{std}$ under the linear map that sends $a$ to the function $x \mapsto \sum_i a_i \chi(x_i)$, and let $h_\chi = a_\chi^{\vee}$. The image lattice $\mathrm{im}_\tau(\chi)$ is the second projection of $\Delta_\tau \cap (h_\chi \times \Omega^{s(\tau)})$, and the kernel lattice $\ker_\tau(\chi)$ is the first projection of $\Gamma_\tau \cap (\Omega^{r(\tau)} \times h_\chi)$.

**Definition 8.12.2 (Test point).** Let $R \subset \Omega$ be a subring. A test point for $R$ at $p$ is a field $C$ over $\Omega$ with a subring $R_C$ such that $C$ is algebraically closed, $R_C = \{c : v(c) \le 1\}$ for a valuation $v$ with $v(p) < 1$, $R_C$ is $p$-adically complete, and $R \subset R_C$. A datum $\mathcal{D}$ with characters $\chi_\tau$ and a permutation $\varphi$ of the labels satisfies the test facts over $R_C$ at $(p, w)$ if for every $\tau$: $w\,\mathrm{std} \subset a_{\chi_\tau}$; $\mathrm{im}_\tau(\chi_\tau) = \omega_\tau$; $\ker_\tau(\chi_\tau) = w^{-1}\mathrm{Lie}_\tau$; the ideals cut out by $a_{\chi_\tau}$ on the coordinate axes equal the ideals cut out by $M$ through $\chi_\tau$; and the step graphs of $\Theta_\tau$ have the expected second projection and, at $\varphi(\tau)$, the expected fibre over $0$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.IsTestPt`.

The test facts are the facts of [the Chern-Weil chapter](/entry/arakelov-geometry/chern-weil/#eigenspace-splitting-on-normal-models), listed above.

The base change of $\mathcal{D}$ to $R_C$ is the datum of the $R_C$-spans of the images of its lattices in $C$.

### The sequence hypotheses at a chart

Let $\mathfrak{M}$ be a Hodge component of $Y$ over $S$ on coordinates $y$, and let $p \in S$ be a prime at which $\mathfrak{M}$ is Hodge-Tate free, with $p \ne 2$ and $p \nmid d_E$. Let $O$ be a discrete valuation ring at a place of $\Omega$ over $p$, and let $w \in O$ with $w = \zeta - 1$ for a primitive $p$-th root of unity $\zeta$. Let $G$ be a torsion datum of $\mathfrak{M}$ at $p$, let $c'$ be a chart with non-zero Segre coordinate, and let $P$ be a chart pack of $G$ over $O$ at $c'$, with its map $q$. For a label $t$, let $\mathrm{HT}_t$ be the coordinate lattice of the Hodge-Tate lattice of $t$ on the chart, in the basis $b_t$, and let $R_{c'}$ be the ring of the chart.

**Definition 8.12.3 (Sequence hypotheses).** A linear map $i \colon \Omega^{r} \to \Omega^{N}$ satisfies the sequence hypotheses for $(R, w, W, \omega, q)$ if $i(W) \subset \mathrm{std}$, $q(\mathrm{std}) \subset \omega$, $i(a) \in w\,\mathrm{std}$ implies $a \in wW$, $q(b) \in w\omega$ holds if and only if $b - i(a) \in w\,\mathrm{std}$ for some $a \in W$, and $\omega \subset q(\mathrm{std}) + w\omega$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.FamEx.SeqHyp`.

These conditions say that $W \to \mathrm{std} \to \omega$ is exact modulo $w$ and that $q$ is onto modulo $w$. The dual sequence condition of $P$ at an embedding $\sigma_E$ and an exponent $m$ is a congruence modulo $p^m$ between the Gram matrix of $P$ at $\sigma_E$ and the hermitian form of $\mathfrak{M}$. We do not unfold it.

**Theorem 8.12.4 (Sequence hypotheses at a chart).** Assume the Hodge-Tate statement of Fargues. In the setting above, for every label $t$ there is a linear map $i \colon \Omega^{r(t)} \to \Omega^N$ that satisfies the sequence hypotheses for $(R_{c'}, w, \mathrm{HT}_t, \mathrm{HT}_{\bar t}^{\vee}, q)$, and such that the dual sequence condition holds with exponent $R(p) - 2$ at every embedding $\sigma_E \colon E \to \Omega$ that agrees with the embedding of $t$ on $\mathcal{O}_E$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.FamEx.Seq.seq_holds` (also `GlobalTheory.T.arith_variety_model_prime_degree`, a second name).

*Proof.* First, lemmas on the Hodge-Tate data at $p$ give the values of the embeddings of $t$ and $\bar t$ on the chart, and their compatibility with complex conjugation on $E$. The Hodge-Tate statement of Fargues enters through a lemma on the chart pack $P$. Since $w = \zeta - 1$, we have $p^2 = w u$ with $u$ integral, so $w$ divides $p^2$. The Hodge component has $R(p) \ge 4$, so $w\,p^{R(p) - 2}$ divides $p^{R(p)}$. The chart sequence of $P$ holds, and a count of the ranks of the labels matches it with $\mathrm{HT}_t$ and $\mathrm{HT}_{\bar t}^{\vee}$. A lemma on Hodge charts then gives a map $i$ with the sequence hypotheses and with a congruence of the Gram matrix modulo $p^{R(p)}$. Since $w\,p^{R(p)-2}$ divides $p^{R(p)}$, this congruence gives the dual sequence condition with exponent $R(p) - 2$. $\square$

### Test orders and test group points

**Corollary 8.12.5 (Test orders are tight).** Assume the Hodge-Tate datum statement and the ordinary curve statement. In the setting of [Theorem 7.9.8](/entry/tight-hopf-order-test/), the test order of $P$ over $R_C$ is an abelian factor and is tight.

Lean: `GlobalTheory.CompanionTheory.Relay.arith_variety_model_hodge_relay` (also `GlobalTheory.T.arith_variety_model_hodge_relay`, a second name).

*Proof.* This is [Theorem 7.9.8](/entry/tight-hopf-order-test/). $\square$

**Corollary 8.12.6 (Test group points).** Assume the five published results. In the setting of [Theorem 7.9.9](/entry/test-group-point-exists/), let $\tau$ be a label and $h_b \colon C^r \to C^N$ an injective linear map with image the kernel of the base change of $q$, such that the pull back of $\mathrm{std}$ by $h_b$ is $W'_\tau$ and $h_b(a) - i_\tau(a) \in w\,\mathrm{std}$ for $a \in W'_\tau$. Then $q(h_{\chi_\tau}) = \omega'_\tau$ and $h_b^{-1}(h_{\chi_\tau}) = w^{-1}\mathrm{Lie}'_\tau$.

Lean: `GlobalTheory.CompanionTheory.Relay.ordinary_curve_model_relay` (also `GlobalTheory.T.ordinary_curve_model_relay`, a second name).

*Proof.* This is [Theorem 7.9.9](/entry/test-group-point-exists/). $\square$

### The test facts

**Theorem 8.12.7 (Test facts).** Assume the five published results. Let $\mathfrak{M}$, $p$, $O$, $w$ with $w^{p-1} = u p$ for a unit $u$, the labels with the Frobenius orbit data and the sections, $G$, $c'$, $P$ and maps $i_\tau$ be as above, and assume that each $i_\tau$ satisfies the sequence hypotheses and the dual sequence condition of the last theorem and that the chart datum $\mathcal{D}$ built from $P$ and $i$ satisfies the base conditions. Let $(C, R_C)$ be a test point for $R_{c'}$ at $p$, and let $\chi_\tau \colon F \to C$ be multiplicative maps such that $\chi_\tau(a) - o \in R_C$ is not a unit of $R_C$ whenever $o \in O$ reduces to $\sigma_\tau(a)$. Then the base change of $\mathcal{D}$ to $R_C$ satisfies the test facts with the characters $\chi_\tau$ and the Frobenius $\varphi'$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.FamEx.TestPt.testFacts` (also `GlobalTheory.T.ordinary_curve_hodge_prime`, a second name).

*Proof.* The field $\Omega$ has characteristic $0$, and so does $C$. The base conditions over $R_{c'}$ pass to the larger ring $R_C$. From $w^{p-1} = up$ and $p \ne 0$ we get $w \ne 0$ in $C$. The torsion datum gives, at the test point, an abelian factor and a group that is tight, by the [corollary on test orders](/entry/relay-arith-variety-model-hodge-relay/). Zarhin's statement, the statement on quotients and the Hodge-Tate datum statement show that the abelian factor and the tight group carry a field action with the expected flags, and the lattice $\Theta_\tau$ maps the square ideal into itself. This gives $w\,\mathrm{std} \subset a_{\chi_\tau}$. The Hodge estimate at the prime and the [corollary on test group points](/entry/relay-ordinary-curve-model-relay/) give the two equalities of the lattice $h_{\chi_\tau}$, and the kernel and image lemma for Hodge lattices turns them into $\mathrm{im}_\tau(\chi_\tau) = \omega_\tau$ and $\ker_\tau(\chi_\tau) = w^{-1}\mathrm{Lie}_\tau$. The remaining facts, on the coordinate ideals and on the step graphs of $\Theta_\tau$, are computed from the base conditions and the values of $\chi_\tau$. $\square$

### The families

A pre-family at $(p, w, \sigma, \varphi)$ is a choice of a datum $\mathcal{D}_c$ for every chart $c$ whose lattices form lattice families in $c$, with these conditions: $p \ne 0$ in $O$, $w^{p-1} = up$ for a unit $u$, $p$ is not a unit; every $\mathcal{D}_c$ on a chart with non-zero Segre coordinate satisfies the base conditions over the ring of the chart; and the base change of $\mathcal{D}_c$ satisfies the test facts at every test point, for all characters $\chi_\tau$ that lift $\sigma_\tau$ as in the last theorem. It is a family of $\mathfrak{M}$ if on every such chart $\mathrm{Lie}_\tau$ and $W_\tau$ are the coordinate lattices of the de Rham and the Hodge-Tate lattices of $\tau$, and $\omega_\tau$ and $\omega^{\mathrm{HT}}_\tau$ are the duals of the coordinate lattices at $\bar\tau$.

**Theorem 8.12.8 (Lattice families at odd primes).** Assume the five published results. Let $\mathfrak{M}$ be a Hodge component of a model $Y$ over $S$ on coordinates $y$ with an arithmetic variety of dimension $d + 1$, with $0 < p + q$, and with bases $b_t$ of the generic spaces of the labels. Let $p \in S$ be a prime with $\mathfrak{M}$ Hodge-Tate free at $p$, $p \ne 2$ and $p \nmid d_E$. Let $\varphi$ be a Frobenius permutation of the labels at $p$ and $A$ the integral closure of $\mathbb{Z}$ in $\Omega$. Then at every discrete valuation ring $O$ that localizes $A$ at a prime over $p$, and for every label $t_0$, there are a finite set $\Sigma$, a map $e \colon \Sigma \to \Phi \sqcup \Phi$ with $t_0$ in its image, a permutation $\varphi'$ of $\Sigma$ with $e \circ \varphi' = \varphi \circ e$, a finite field $F$ of characteristic $p$, $w \in O$, embeddings $\sigma_\tau$ of $F$ into the residue field of $O$, and data $\mathcal{D}_c$, that form a pre-family and a family of $\mathfrak{M}$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.FamEx.familyExistsPos_holds` (also `GlobalTheory.T.family_pos_of_hodge_tate_inputs`, a second name).

*Proof.* A first lemma at the prime gives the labels $\Sigma$, $e$, $\varphi'$, $F$, the ranks, the sections, $w$, $\sigma$ and the orbit conditions; the orbit conditions give $w = \zeta - 1$. Further lemmas give a torsion datum $G$ and chart packs $P$ over $O$ at every chart. The Hodge-Tate statement of Fargues gives the lattice families and their inclusions, and the [sequence hypotheses theorem](/entry/arith-variety-model-prime-degree/) gives maps $i$ with the sequence hypotheses and the dual sequence condition at each chart. We have $w \ne 0$. A count of ranks and a lemma that turns the sequence hypotheses into the conditions on $\Gamma$ and $\Delta$, through the short exact sequence of the standard lattice, give the base conditions, and the families of $M$, $\Gamma$, $\Delta$ and $\Theta$ come from the total degree of the torsion and the model at the prime. The test clause is the [theorem on test facts](/entry/ordinary-curve-hodge-prime/). $\square$

**Remark 8.12.9 (Formalization).** The five published results enter as hypotheses of type `Prop`. In the caller FinalTheoremOfInputsRight.lean:35, the Hodge-Tate datum statement and the ordinary curve statement are proved, and the first three stay as hypotheses. The relays `Relay.arith_variety_model_hodge_relay` and `Relay.ordinary_curve_model_relay` are second names of `PositivityTheory.Xgn.tight_hopf_order_test` and `PositivityTheory.Xgn.test_group_point_exists` (ArithVarietyModelHodgeRelay.lean:13, OrdinaryCurveModelRelay.lean:13), so the names under `T` are second names of second names. Many names do not describe their statements: `T.ordinary_curve_hodge_prime` proves the test facts, and `T.arith_variety_model_prime_degree` proves the sequence hypotheses. The proofs set `maxHeartbeats` to 1000000 for a proof of one line (FamilyPosOfHodgeTateInputsStatement.lean:19) and to 4000000 (OrdinaryCurveHodgePrime.lean:53). The steps go through named results such as `T.arith_variety_hodge_prime_bound`, `T.arith_variety_model_prime_bound`, `T.lattice_base_change_larger_ring_holds` and `T.hodge_kernel_image_lattice`, and through the dual sequence condition `DualSeq`, which we do not unfold.
