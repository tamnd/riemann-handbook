---
title: Homotopy invariance
decls:
  - GlobalTheory.EtC.HomotopyInv.homotopy_invariance_etale
  - GlobalTheory.T.homotopyInvariance_tateTwist_strictlyHenselian
  - GlobalTheory.homotopyInvariance_strictlyHenselian
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Homotopy invariance

This section proves that the [étale cohomology](/learn/geometry/#tale-cohomology) of a ring $A$ with coefficients $\mathbb{Z}/q(i)$ does not change when we pass from $A$ to the polynomial ring $A[t]$, provided that $q$ is a unit in $A$. For schemes this is the classical homotopy invariance of étale cohomology with coefficients prime to the residue characteristics, a consequence of the smooth base change theorem (SGA 4, Exposé XV, §2). Here we deduce it from results on integral maps, on dimension and on filtered colimits, by an induction on the Krull dimension of rings of finite type over $\mathbb{Z}$.

We keep the notation of the earlier sections. For a ring $A$ we write $H^n(A, F)$ for the cohomology of $\mathrm{sp}(A)$ with coefficients in $F$, and $x \mapsto x|_{A'}$ for the pullback along a ring map $A \to A'$. A ring is *strictly henselian* if it is a henselian local ring with [[separably closed|8B57B7EGK4]] residue field. The Krull dimension $\dim R$ of a ring takes values in $\{-\infty\} \cup \mathbb{N} \cup \{\infty\}$, and $\dim R = -\infty$ exactly when $R$ is the zero ring.

**Definition 2.13.1 (Homotopy invariant ring).** Let $q \geq 1$. A ring $A$ is *homotopy invariant for $q$* if for every $i \in \mathbb{Z}$ and every $n$ the pullback along the inclusion of constants $A \to A[t]$,
$$
H^n(A, \mathbb{Z}/q(i)) \longrightarrow H^n(A[t], \mathbb{Z}/q(i)),
$$
is bijective.

Lean: `GlobalTheory.EtC.HInv`.

### Inputs

We use the following results and take them as given.

**Lemma 2.13.2 (Reduction to strictly henselian bases).** Let $q$ be a natural number, let $f : Y \to X$ and $p : X \to S$ be quasi-compact and quasi-separated maps of schemes, suppose that $q$ is a unit in $\Gamma(S, \mathcal{O}_S)$, and let $i \in \mathbb{Z}$. Suppose that for every strictly henselian ring $A'$ and every map $s : \operatorname{Spec} A' \to S$ the base change
$$
f_s : Y \times_S \operatorname{Spec} A' \longrightarrow X \times_S \operatorname{Spec} A'
$$
induces bijections $H^n(X \times_S \operatorname{Spec} A', \mathbb{Z}/q(i)) \to H^n(Y \times_S \operatorname{Spec} A', \mathbb{Z}/q(i))$ for every $n$. Then $f$ induces bijections $H^n(X, \mathbb{Z}/q(i)) \to H^n(Y, \mathbb{Z}/q(i))$ for every $n$.

Lean: `GlobalTheory.T.etC_b3`.

The stalks of the higher direct images of a sheaf along $p$ are computed on the strict henselisations of the local rings of $S$, so a map that is an isomorphism on these is an isomorphism on $S$.

**Lemma 2.13.3 (Base change of the polynomial ring).** Let $A$ and $A'$ be rings, let $s : \operatorname{Spec} A' \to \operatorname{Spec} A$ be a map of schemes, let $q$ be a natural number and let $i \in \mathbb{Z}$. Suppose that the inclusion of constants $A' \to A'[t]$ induces bijections $H^n(A', \mathbb{Z}/q(i)) \to H^n(A'[t], \mathbb{Z}/q(i))$ for every $n$. Then the base change of $\operatorname{Spec} A[t] \to \operatorname{Spec} A$ along $s$,
$$
\operatorname{Spec} A[t] \times_{\operatorname{Spec} A} \operatorname{Spec} A' \longrightarrow \operatorname{Spec} A \times_{\operatorname{Spec} A} \operatorname{Spec} A',
$$
induces bijections on $H^n(-, \mathbb{Z}/q(i))$ for every $n$.

Lean: `GlobalTheory.PolynomialPushoutEquivalence.main`.

The two fibre products are $\operatorname{Spec} A'[t]$ and $\operatorname{Spec} A'$, and the map between them is $\operatorname{Spec}$ of the inclusion of constants $A' \to A'[t]$.

**Lemma 2.13.4 (The zero ring).** Let $q \geq 1$. The zero ring is homotopy invariant for $q$.

Lean: `GlobalTheory.T.etaleHomotopyInvariantTwists_of_subsingleton`.

**Lemma 2.13.5 (Directed unions).** Let $q \geq 1$ and let $A$ be a ring. Let $I$ be a nonempty directed preordered set and let $(S_j)_{j \in I}$ be an increasing family of subrings of $A$ with union $A$. Suppose that $q$ is a unit in every $S_j$ and that every $S_j$ is homotopy invariant for $q$. Then $A$ is homotopy invariant for $q$.

Lean: `GlobalTheory.T.hInv_of_directed_union_subalgebras`.

Étale cohomology commutes with filtered colimits of rings (SGA 4, Exposé VII, §5), and $A[t]$ is the union of the subrings $S_j[t]$.

**Lemma 2.13.6 (Descent along integral maps).** Let $q \geq 1$ and let $A \to B$ be an integral ring map whose kernel is contained in the [[nilradical|QQDN6EYQNJ]] of $A$. Suppose that $q$ is a unit in $A$ and that the tensor power $B^{\otimes_A (k+1)}$ is homotopy invariant for $q$ for every $k \geq 0$. Then $A$ is homotopy invariant for $q$.

Lean: `GlobalTheory.T.etaleHomotopyInvariance_cechDescent_integral`.

The kernel condition makes $\operatorname{Spec} B \to \operatorname{Spec} A$ surjective. The lemma on descent along integral surjections of the section on the punctured line then computes the cohomology of $A$ and of $A[t]$ from the Čech nerves of $\operatorname{Spec} B \to \operatorname{Spec} A$ and of $\operatorname{Spec} B[t] \to \operatorname{Spec} A[t]$, whose levels are the tensor powers of $B$ and of $B[t]$, and $B^{\otimes_A (k+1)}[t] = B[t]^{\otimes_{A[t]} (k+1)}$.

**Lemma 2.13.7 (Tensor powers of the absolute integral closure).** Let $q \geq 1$ and $d \in \mathbb{N}$. Suppose that every ring $R$ of finite type over $\mathbb{Z}$ with $q$ a unit in $R$ and $\dim R < d$ is homotopy invariant for $q$. Let $D$ be a domain of finite type over $\mathbb{Z}$ with $q$ a unit in $D$ and $\dim D \leq d$, and let $B$ be the [[integral closure|G0V86SJBQW]] of $D$ in an [[algebraic closure|0X6AB5P3G1]] of the fraction field of $D$. Then $B^{\otimes_D (k+1)}$ is homotopy invariant for $q$ for every $k \geq 0$.

Lean: `GlobalTheory.T.etale_homotopy_invariance_tensor_power_integral_closure`.

**Lemma 2.13.8 (From domains to all rings).** Let $q \geq 1$ and $d \in \mathbb{N}$. Suppose that every ring $R$ of finite type over $\mathbb{Z}$ with $q$ a unit in $R$ and $\dim R < d$ is homotopy invariant for $q$, and that every domain $D$ of finite type over $\mathbb{Z}$ with $q$ a unit in $D$ and $\dim D \leq d$ is homotopy invariant for $q$. Then every ring $R$ of finite type over $\mathbb{Z}$ with $q$ a unit in $R$ and $\dim R \leq d$ is homotopy invariant for $q$.

Lean: `GlobalTheory.T.etaleHomotopyInvariantTwists_of_domains_of_dim_lt`.

**Lemma 2.13.9 (Finite dimension).** A ring essentially of finite type over $\mathbb{Z}$ has finite Krull dimension.

Lean: `GlobalTheory.ringKrullDim_lt_top_of_essFiniteType`.

A ring of finite type over $\mathbb{Z}$ is a quotient of $\mathbb{Z}[x_1, \dots, x_m]$, which has dimension $m + 1$, and localization does not raise the dimension.

### Strictly henselian rings

**Theorem 2.13.10 (Homotopy invariance over a strictly henselian ring).** Let $q \geq 1$, let $A$ be a strictly henselian ring in which $q$ is a unit, and let $i \in \mathbb{Z}$. Then the pullback along $A \to A[t]$ induces bijections
$$
H^n(A, \mathbb{Z}/q(i)) \longrightarrow H^n(A[t], \mathbb{Z}/q(i))
$$
for every $n$.

Lean: `GlobalTheory.homotopyInvariance_strictlyHenselian` (also `GlobalTheory.T.homotopyInvariance_tateTwist_strictlyHenselian`).

*Proof.* We show that $A$ is homotopy invariant for $q$. The argument does not use that $A$ is strictly henselian.

Step 1 (rings of finite type). We prove by induction on $d \in \mathbb{N}$ the claim $P(d)$: every ring $R$ of finite type over $\mathbb{Z}$ with $q$ a unit in $R$ and $\dim R < d$ is homotopy invariant for $q$.

For $d = 0$, the condition $\dim R < 0$ says that $R$ has no prime ideal. A nonzero ring has a maximal ideal, so $R$ is the zero ring, and the lemma on the zero ring applies.

Suppose $P(d)$ holds, and let $R$ be of finite type over $\mathbb{Z}$ with $q$ a unit in $R$ and $\dim R < d + 1$. Since $\dim R$ is $-\infty$, a natural number or $\infty$, this gives $\dim R \leq d$. First let $D$ be a domain of finite type over $\mathbb{Z}$ with $q$ a unit in $D$ and $\dim D \leq d$. Let $K$ be the fraction field of $D$, $\bar{K}$ an algebraic closure of $K$, and $B$ the integral closure of $D$ in $\bar{K}$. The map $D \to B$ is integral by the definition of $B$. It is injective, because $D \to K$ and $K \to \bar{K}$ are injective; so its kernel is $0$, which lies in the nilradical. By $P(d)$ and the lemma on tensor powers, every $B^{\otimes_D (k+1)}$ is homotopy invariant for $q$. The lemma on descent along integral maps gives that $D$ is homotopy invariant for $q$. Now $P(d)$ and the statement for domains of dimension at most $d$ are the hypotheses of the lemma from domains to all rings, which gives that $R$ is homotopy invariant for $q$. This proves $P(d + 1)$.

Step 2 (finitely generated subrings). Let $u = q^{-1} \in A$. For a finite subset $s \subseteq A$ let $S_s$ be the subring of $A$ generated by $u$ and $s$. Then $S_s \subseteq S_{s'}$ when $s \subseteq s'$, and $a \in S_{\{a\}}$ for every $a \in A$. The finite subsets of $A$, ordered by inclusion, form a nonempty directed set, and the union of the $S_s$ is $A$. The element $q$ is a unit in $S_s$, with inverse $u$. The ring $S_s$ is generated by finitely many elements, so it is of finite type over $\mathbb{Z}$. By the lemma on finite dimension, $\dim S_s \leq d$ for some $d \in \mathbb{N}$, so $\dim S_s < d + 1$, and $P(d + 1)$ from Step 1 says that $S_s$ is homotopy invariant for $q$.

Step 3 (conclusion). The lemma on directed unions applies to the family $(S_s)$ and gives that $A$ is homotopy invariant for $q$. Taking the given $i$, the pullback is bijective for every $n$. $\square$

### All rings

**Theorem 2.13.11 (Homotopy invariance).** Let $q \geq 1$, let $A$ be a ring in which $q$ is a unit, and let $i \in \mathbb{Z}$. Then the pullback along $A \to A[t]$ induces bijections
$$
H^n(A, \mathbb{Z}/q(i)) \longrightarrow H^n(A[t], \mathbb{Z}/q(i))
$$
for every $n$.

Lean: `GlobalTheory.EtC.HomotopyInv.homotopy_invariance_etale`.

*Proof.* Let $f : \operatorname{Spec} A[t] \to \operatorname{Spec} A$ be the map given by the inclusion of constants, and let $p$ be the identity of $S = \operatorname{Spec} A$. Both maps are maps of affine schemes, so they are quasi-compact and quasi-separated. The ring $\Gamma(S, \mathcal{O}_S)$ is $A$, so $q$ is a unit in it. We check the hypothesis of the lemma on reduction to strictly henselian bases. Let $A'$ be a strictly henselian ring and $s : \operatorname{Spec} A' \to \operatorname{Spec} A$ a map. The map $s$ comes from a ring map $A \to A'$, which sends the unit $q$ to a unit, so $q$ is a unit in $A'$. The [theorem over a strictly henselian ring](/entry/homotopy-invariance-strictly-henselian/) gives bijections $H^n(A', \mathbb{Z}/q(i)) \to H^n(A'[t], \mathbb{Z}/q(i))$ for every $n$. The lemma on base change of the polynomial ring turns these into bijections for the base change $f_s$ of $f$ along $s$. The lemma on reduction to strictly henselian bases now gives that $f$ induces bijections $H^n(A, \mathbb{Z}/q(i)) \to H^n(A[t], \mathbb{Z}/q(i))$ for every $n$. $\square$

Since the proof of the theorem over a strictly henselian ring works for every ring in which $q$ is a unit, it gives the theorem for all rings directly. The reduction to strictly henselian bases is the route that a proof by the smooth base change theorem would take.

**Remark 2.13.12 (Formalization).** The theorem for all rings is the condition $C_4$ of the package of axioms on étale cohomology in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L113). The proof of the theorem over a strictly henselian ring introduces the hypothesis that $A$ is strictly henselian and does not use it: [HomotopyInvarianceTateTwistStrictlyHenselian.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HomotopyInvarianceTateTwistStrictlyHenselian.lean#L14). In [HomotopyInvarianceEtale.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HomotopyInvarianceEtale.lean#L14) a lemma on the composition of two maps that induce bijections is proved and not used, and the base change step tries six tactics in turn at lines 28 to 34. The wrapper [HomotopyInvarianceTateTwistStrictlyHenselianStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HomotopyInvarianceTateTwistStrictlyHenselianStatement.lean#L5) raises the heartbeat limit. We opened the statements of the lemmas of the inputs but not their proofs; the reasons we give after them are ours.
