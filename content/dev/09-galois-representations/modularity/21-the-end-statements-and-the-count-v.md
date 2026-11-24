---
title: The end statements and the count V
decls:
  - UpperTheory.V.Z.Win.Dn.ends_of_alt
  - UpperTheory.V.Z.Win.Dn.ends_u_alt
  - UpperTheory.V.Z.Win.Dn.ends0_alt
  - UpperTheory.V.UnitaryThreeInertia.countV_of_finiteness_duality_euler_host
  - UpperTheory.V.Z.J.count_v_of_printed_bound_k_reduced_unitary_lift
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The end statements and the count V

This section proves the two facts of Step 2 of section 1, the end statement for the residual images and the core statement for case V, and then proves the count V of Step 5. Both facts are about unitary three-dimensional representations of $G_{\mathbb{Q}}$ whose restriction to an imaginary quadratic field is conjugate self-dual. The end statement says that the deformation rings of such representations are finite at their ends and that their points are automorphic. The core statement says that the weight zero part of a universal deformation ring of a host frame is finite and that its points of type I are automorphic. The count V then bounds the length of case V by the congruences between the reducible point $r_0$ and the automorphic points of the universal ring. The input that ties both facts to the rest of the chapter is the [Theorem 8.20.7](/entry/linked-unl-e-alt/) of section 20: the points of case V are unlinked at the places above $l$.

Let $K$ be an imaginary quadratic field with quadratic character $\eta$, and let $\Psi$ be the character $\chi_{\mathrm{cyc}}^{e} \psi$ for a Dirichlet character $\psi$ modulo $N$ and $e \ge 1$. A host frame $F$ is a frame on the Galois group $\Gamma_S$ of the maximal extension of $\mathbb{Q}$ unramified outside the primes $S$ that divide $l N$, with the characters $\eta$ and $\Psi$. Its residual point $r_0$ is a reducible three-dimensional representation built from $\eta$ and $\Psi$. A point of type I of a universal ring for $F$ is a point $r$ over $\overline{\mathbb{Q}}_l$ of the shape of case I relative to $\eta$.

**Definition 8.21.1 (End statement).** The end statement holds if, for every CM field $K$, every datum $D$ of characters $\eta$ and $\Psi$ and a complex conjugation over $K$, every $\iota \colon \overline{\mathbb{Q}}_l \cong \mathbb{C}$ and every valuation ring $B$ of $\Omega$ above $l$, there is a marked element $g_1$ such that the deformation ring of $D$ with mark $g_1$ is finite at its end, its three-dimensional points at the end are automorphic over $K$, and its two-dimensional points at the end are automorphic.

**Definition 8.21.2 (Core statement for case V).** The core statement holds if, for every imaginary quadratic field $K$, every host datum and every host frame $F$, there is a marked $g_1 \in \Gamma_S$ such that for every universal deformation $u$ of $F$ with mark $g_1$ and ring $R$, two things hold: the weight zero part of $R$ is finite over $\mathcal{O}$, and each point $r$ of type I of $R$ is automorphic over $K$, in the sense that $r|_{G_K}$ is attached through $\iota$ to a conjugate self-dual cuspidal representation of $\mathrm{GL}_3(\mathbb{A}_K)$ with the twist by $-1$.

The strong form of the core statement asks also that each point of type I be irreducible on every open subgroup of $\ker \eta$ and on $\ker \eta \cap \ker \chi_{\mathrm{cyc}}$.

**Theorem 8.21.3 (End statements from unlinkedness).** Assume the extended hypotheses. Suppose that the points of case V are unlinked, and that the end points of the rank three family are linked to their ends (the statement of linked ends). Then the end statement and the core statement for case V hold.

Lean: `UpperTheory.V.Z.Win.Dn.ends_of_alt`.

*Proof.* Unlinkedness gives the local condition in rank three at even level: at the places above $l$, the points of the family have distinct inertia characters that are not linked. With the inertia and ordinarity conditions, this gives the local condition for links in rank three, and in the same way the inertia condition in rank two. The extended hypotheses give the global compatibility of the Galois representations of the literature, which provides good data and host data. They also give the descent of conjugate self-dual representations over $K$, the automorphy of newforms, and the twist and algebraicity conditions. The end statement then follows from the descent theorem for good data, applied with these local conditions, potential automorphy in rank two and the linked ends. The core statement follows from the symmetric cube theorem for endomorphisms, applied to the host frame with the local condition in rank three, the linked ends and the descent over $K$. $\square$

**Corollary 8.21.4 (End statements).** Assume the extended hypotheses and the unlinkedness of the points of case V. Then the end statement and the core statement for case V hold. Under the extended hypotheses alone, both hold.

Lean: `UpperTheory.V.Z.Win.Dn.ends_u_alt` (also `UpperTheory.V.Z.Win.Dn.ends0_alt`, the form under the extended hypotheses alone).

*Proof.* The linked ends follow from the extended hypotheses, the seed in rank two and unitary three-dimensional automorphy (section 14), so the theorem applies. Under the extended hypotheses, the [Theorem 8.20.7](/entry/linked-unl-e-alt/) of section 20, with the same seed and the same automorphy, gives unlinkedness. $\square$

This is Step 2 of section 1. The two halves are used in different places: the end statement in the count I, through the automorphy of unramified representations, and the core statement in the count V below.

**Theorem 8.21.5 (Count V from a host frame).** Assume the following.

1. The strong core statement for case V.
2. The lemmas M and M'.
3. The six facts of Galois cohomology: local finiteness, local Tate duality, the local Euler characteristic formula, global finiteness, the global Euler characteristic formula and Poitou-Tate duality.
4. Two facts for each host frame $F$: the cocycles of $r_0$ of weight at most zero vanish, and the Selmer quotient of weight $-2$ has at most one element.
5. Rigidity: each point in characteristic zero with the properties of the strong core statement is rigid.
6. The point count: there are $C$ and $\varphi \in \Gamma_S$ with $\operatorname{tr} r(\varphi) \ne \operatorname{tr} r_0(\varphi)$ for each good point $r$, such that for good points $r_1, \dots, r_n$ that are pairwise not isomorphic on $\ker \eta$,

$$\log l \sum_{i=1}^{n} v_l\bigl(\operatorname{tr} r_i(\varphi) - \operatorname{tr} r_0(\varphi)\bigr) \le (l N e)^{C}.$$

Then the count V holds.

Lean: `UpperTheory.V.UnitaryThreeInertia.countV_of_finiteness_duality_euler_host`.

*Proof.* Fix the primitive character $\chi$. Let $K = \mathbb{Q}(i)$; the point count for $K$ gives $C$, and we prove the count with exponent $C + 1$. Let $l$, $e$ and $\psi$ be as in case V. The host data of $\psi$ give a host frame $F$, and we choose $\iota$. The strong core statement gives the mark $g_1$, and the frame gives a universal deformation $u$ with mark $g_1$; its weight zero part is finite, and its points of type I have the properties of the strong core statement. Now the [Theorem 7.7.4](/entry/abstract-count/) on abstract counts applies. Its inputs are the lemmas M and M', the local vanishing at the frame, the count at the frame, the vanishing of fact 4, the class number one of $K$, the Selmer quotient of fact 4, rigidity and $\varphi$. It gives good points $r_1, \dots, r_n$, pairwise not isomorphic on $\ker \eta$, and a number $V$ such that the length of each nonzero class is at most $V$ and

$$V \le 2\, e_{\mathcal{O}} \sum_{i=1}^{n} v_l\bigl(\operatorname{tr} r_i(\varphi) - \operatorname{tr} r_0(\varphi)\bigr),$$

where $e_{\mathcal{O}}$ is the length of $\mathcal{O}/l$. The length $V_{\mathrm{len}}(e, \psi)$ is at most $V$. With $X = l N e \ge 2$, the point count gives

$$\frac{V_{\mathrm{len}}(e, \psi)}{e_{\mathcal{O}}} \log l \le 2 X^{C} \le X^{C+1}. \qquad \square$$

**Theorem 8.21.6 (Count V).** Assume the extended hypotheses, Lemma K and the core statement for case V. Then the count V holds.

Lean: `UpperTheory.V.Z.J.count_v_of_printed_bound_k_reduced_unitary_lift`.

*Proof.* We supply the inputs of the [Theorem 8.21.5](/entry/count-v-of-finiteness-duality-euler-host/). The strong core statement follows from the core statement, since the two irreducibility conditions hold for points of type I of a reduced unitary lift. The lemmas M and M' are proved in the algebraic part of the chapter. The six facts of Galois cohomology are part of the extended hypotheses. The vanishing of fact 4 follows from Lemma K, and the bound on the Selmer quotient follows from the corollary X, the lemma X and the nonvanishing of a residual Bernoulli number. Rigidity and the point count follow from the end statement for unlinked points, which comes from the [Theorem 8.20.7](/entry/linked-unl-e-alt/) of section 20 with the adjoint lifting theorem. $\square$

**Remark 8.21.7 (Formalization).** The two parts of the end statement are proved by `gdEnd_of_frame_linkedEnd_downCsdK_descent` and `symmetric_cube_theorem_of_endomorphisms_alt` ([DnEnds.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/DnEnds.lean#L35)); our account of these two proofs reads their inputs, which we have not unfolded. The end statement is `GdEndAlt` ([AutEnd3AltAlt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/AutEnd3AltAlt.lean#L35)), with the clauses `Marks`, `FinEnd`, `AutEnd3Alt` and `AutEnd2Ao`; the core statement and its strong form are `ThmS6Core_s` and `ThmS6_s` ([ThmS6CoreS.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ThmS6CoreS.lean#L17)). The count V from Lemma K computes `unlEnd3E (linkedUnlE_alt hH)` at [LinkedUnlE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean#L57), and the count I in the same file computes it again at line 51. The private lemmas `arith` and `l_mem` of the count from a host frame are copies of lemmas in [UnitaryThreeDeformations/CountVOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/CountVOf.lean#L19), a file with nothing else. We have not unfolded `Frame`, `IsUniv`, `TypeI` or `HostData`, nor the residual point $r_0$.
