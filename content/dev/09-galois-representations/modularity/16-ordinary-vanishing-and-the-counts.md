---
title: Ordinary vanishing and the counts
decls:
  - UpperTheory.V.Th.core_o_of_literal_automorphy_n
  - UpperTheory.V.Th.ordinary_vanishing_two_of_printed_hida
  - UpperTheory.V.Th.core_alt_bis
  - UpperTheory.V.Th.sp4Main_alt
  - UpperTheory.V.HV.DescentVanishingReductions.countII_and_countIII_of_printsH_of_sp4In
  - UpperTheory.V.HV.Core.of_four_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Ordinary vanishing and the counts

This section closes the argument of section 1. First we prove the adjoint lifting theorem that section 10 takes as given: under the extended hypotheses, an ordinary cocycle of the adjoint of an automorphic point of a Hida family is a coboundary. Then we prove the counts II and III from the symplectic image statement of section 11 and Lemma K of section 15. Last, we show how Lemma K and the counts give [the window bound](/proof/vwin/). We keep the Hida setting of section 10: $l$ is an odd prime, $L$ is a CM field, $S$ is the set of places of the setting, $r$ is a residual representation of rank $n$ with $2 \le n \le 4$, $B$ is its universal ordinary determinant ring, and a point $x$ of $B$ has characters $\psi_{v,i}$ at the places $v$ above $l$.

**Definition 8.16.1 (Ordinary cocycle).** Let $\rho \colon G_{L,S} \to \mathrm{GL}_n(\overline{\mathbb{Q}}_l)$ be continuous. A cocycle $z$ of $\operatorname{ad} \rho$ is ordinary if it is continuous and polarized, zero on the inertia groups at the tame places, and, after a coboundary is subtracted, upper triangular at each place above $l$ in a basis in which $\rho$ is upper triangular.

**Theorem 8.16.2 (Derivations at an ordinary point).** Assume the rank $n$ package. Let $x \colon B \to \mathcal{O}$ be an arithmetic point and $J \subseteq \ker x$ an ideal with the level condition. Let $y$ be a point with representation $\rho_y$ over $\mathcal{O}$ whose determinant and characters are those of $x$, and assume the residual condition at $y$. Let $\sigma_1, \dots, \sigma_q$ be elements of the group $G'$ of the setting such that each $\rho_y(\sigma_j)$ has distinct eigenvalues, and assume that a polarized cocycle $z$ with $\operatorname{tr}(z(\sigma_j) \rho_y(\sigma_j)^k) = 0$ for all $j$ and $k$ is a coboundary. Let $\delta \colon B \to \mathcal{O}$ be an $\mathcal{O}$-linear derivation at $x$ with $\delta(\psi_{v,i}(g)) = 0$ for all $v$, $i$ and $g$ in the inertia group at $v$. Then $\delta(\operatorname{tr} g) = 0$ for every $g$.

Lean: `UpperTheory.V.Th.core_o_of_literal_automorphy_n`.

*Proof.* The rank $n$ package gives the cohomology package. The elements $\sigma_j$ form a frame of the group $G'$. Up to each power of the maximal ideal, $B$ is generated over $\mathcal{O}$ by the values of its pair of trace and characters. For $h$ in the frame, $\rho_y(h)$ is unipotent modulo the maximal ideal $\mathfrak{m}$, so $\rho_y(h)^{l^{a+m}} \equiv 1$ modulo $\mathfrak{m}^m$ for a fixed $a$. So $\rho_y$ is trivial on the intersection of the open normal subgroups that contain a power $h^{l^e}$ of each such $h$. Suppose now $\delta(\operatorname{tr} g_0) \ne 0$. The derivation gives a cocycle with the trace conditions at the $\sigma_j$, and it kills the characters on inertia, so the weight elements of the level condition do not see it. A count of the trace functions of Selmer classes modulo $\mathfrak{m}^m$ bounds their number. Local class field theory, the residual condition and the condition at the $\sigma_j$ enter this bound. For a suitable exponent $m$, the cocycles $l^k \delta$ give more trace functions than the bound allows. This is a contradiction. $\square$

**Theorem 8.16.3 (Ordinary vanishing).** Assume the extended hypotheses. Let $x$ be an arithmetic point of $B$ and $\rho$ a continuous representation with determinant $x$. Suppose that $\rho$ is conjugate self-dual automorphic and trivial on the inertia group at $v_0$, that the matrices $\rho(g)$ span $M_n(\overline{\mathbb{Q}}_l)$, that $\psi_{v,i} \ne \psi_{v,j} \bar\varepsilon$ at each place $v$ above $l$, and that some element has a separable characteristic polynomial. Then each ordinary cocycle $z$ of $\operatorname{ad} \rho$ is a coboundary: $z(g) = \rho(g) Y \rho(g)^{-1} - Y$ for a matrix $Y$.

Lean: `UpperTheory.V.Th.ordinary_vanishing_two_of_printed_hida`.

*Proof.* An ordinary cocycle is a tangent vector to the ordinary deformations of $\rho$. Conjugate $\rho$ to an integral self-dual form, and take integral models of $\rho$ and of a multiple of $z$. They give a point of a universal ring over the dual numbers $\mathcal{O}[\epsilon]/(\epsilon^2)$ and so a derivation $\delta$ at $x$. If $\delta$ kills all traces, then $\operatorname{tr}(z(g) \rho(g)) = 0$ for all $g$, and $z$ is a coboundary because the $\rho(g)$ span all matrices. The extended hypotheses give a Hecke ideal $J$ with the level condition, and the automorphy of $\rho$ with the flags from the ordinarity of $z$ gives $J \subseteq \ker x$. Since $z$ is ordinary, $\delta$ kills the characters on inertia. By the previous theorem, $\delta$ kills all traces. $\square$

**Corollary 8.16.4 (Adjoint lifting).** Assume the extended hypotheses and the cohomology package. Let $L$ contain no primitive $l$-th root of unity, and let $x$ be a point of $B$ whose representation $\rho$ is automorphic, locally generic, irreducible and has a flag at each place above $l$. Then every ordinary cocycle of $\operatorname{ad} \rho$ is a coboundary.

Lean: `UpperTheory.V.Th.core_alt_bis`.

*Proof.* We check the hypotheses of ordinary vanishing. Irreducibility gives the spanning condition. The cohomology package and the residual condition on $r$ give an element with separable characteristic polynomial. Local genericity and the freeness of the characters $\psi_v$ give $\psi_{v,i} \ne \psi_{v,j} \bar\varepsilon$. $\square$

This is the adjoint lifting theorem of section 10, so the eigenbasis theorem there holds under the extended hypotheses.

### The counts II and III

The counts are those of section 1. For a host $h$ with character $\chi$, big for $t$, an odd prime $l$, $0 < e < t$ and a character $\psi$ in case II, the count II asks that the Tate-Shafarevich length $V(e, \psi)$ be finite and that $V(e, \psi) \log l \le (l N e)^C$, with $C$ depending only on $\chi$. The count III is the same in case III. Case II and case III attach two integers $n_{II}(l, \psi)$ and $n_{III}(l, \psi)$ to $\psi$, which depend only on the order, the kernel and the parity of $\psi$ and on two local invariants of $\psi$.

**Theorem 8.16.5 (Counts from the symplectic inputs).** Assume the symplectic image statement, the cohomology package, the three algebraic lemmas M, M' and P, the point count in rank four, rigidity in rank four, the corollary X, and for each $l$ the two bounds on the Selmer lengths of the symplectic family. Then the counts II and III hold.

Lean: `UpperTheory.V.Th.sp4Main_alt`.

The inputs are those of [the main count in rank four](/entry/main-big/). That count gives the bound for $\psi$ in case II or III, but only over a coefficient ring that contains the roots of unity of orders $2^{n_{II}}$ and $2^{n_{III}}$.

*Proof.* Fix $\chi$, and take $C$ from the main count. Let $h$, $l$, a coefficient ring $\mathcal{O}$, $e$ and $\psi$ be given. There is a coefficient ring $\mathcal{O}_1$ with the roots of unity of order $2^{n_{II} + n_{III}}$, and a coefficient ring $\mathcal{O}'$ that contains $\mathcal{O}$ and $\mathcal{O}_1$. Let $f \colon \mathcal{O} \to \mathcal{O}'$ be the inclusion and $\psi' = f \circ \psi$. Since $f$ is injective, $\psi'$ has the same order, kernel, parity and local invariants as $\psi$. So $n_{II}$ and $n_{III}$ do not change, and $\psi'$ is in the same case. The main count gives the bound for $\psi'$ over $\mathcal{O}'$. The lengths depend only on the values of the characters in $\overline{\mathbb{Q}}_l$, so the bound holds for $\psi$. The counts II and III follow by restriction to each case. $\square$

**Corollary 8.16.6 (Counts II and III).** Assume the extended hypotheses, Lemma K with some constant $C_K$, and the symplectic image statement. Then the counts II and III hold.

Lean: `UpperTheory.V.HV.DescentVanishingReductions.countII_and_countIII_of_printsH_of_sp4In`.

*Proof.* We supply the inputs of the theorem. The cohomology package and rigidity in rank four come from the adjoint lifting package of the extended hypotheses. The lemmas M, M' and P and the corollary X are proved, the last one from the nonvanishing of a residual Bernoulli number. The point count comes from the classical part of the extended hypotheses. The two bounds on the Selmer lengths come from Lemma K, Poitou-Tate duality, local finiteness and local Tate duality. $\square$

So Lemma K enters the counts II and III only through the two bounds on Selmer lengths.

### The window from the counts

**Theorem 8.16.7 (Window bound from Lemma K and the counts).** Assume the rank $n$ package, Lemma K with some constant $C_K$, and the counts I, II, III and V. Then the window bound holds.

Lean: `UpperTheory.V.HV.Core.of_four_alt`.

*Proof.* Lemma K, Poitou-Tate duality, local finiteness, local Tate duality and the theorem of Ferrero and Washington (Ann. of Math. 109, 1979) give the window theorem B for the part at $l = 2$ and the parts over the cyclotomic layers. We use it with the exponent $401$. Poitou-Tate duality and a statement of the rank $n$ package give the bound for the minus part of each CM field of the family. The count for case Z holds, because the length is zero in that case. These bounds, Lemma K and the counts I, II, III, V and Z give the window bound, by the splitting of the length into its three parts as in Step 6 of the proof in section 1. $\square$

**Remark 8.16.8 (Formalization).** The theorem `core_alt_bis` in [ThFinal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ThFinal.lean#L17) is the one term `core_of_ord_vanishing_two_phi_all (ordinary_vanishing_two_of_printed_hida hH) (W.phiAll hC)`. In [TCoreOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TCoreOf.lean#L20), the proof of `core_of_ord_vanishing_two_phi_all` binds several hypotheses of the main case to `_`, among them the condition on roots of unity, and does not use them. The count bound that `b1O` proves is named `ordinaryHeckeAlgebraIntegral` in [OrdinaryHeckeAlgebraIntegral.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/OrdinaryHeckeAlgebraIntegral.lean#L208), although no Hecke algebra appears in it, and `CoreO` at line 217 of that file repeats the statement of the main ordinary case with a different level condition. In [ConductorAtMapInjectiveCoeff.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ConductorAtMapInjectiveCoeff.lean#L131), the private lemma `conductor_at_map_injective_coeff` (line 35) is about the multiplicative order `n0` and not a conductor, and `sp4Main_alt` repeats `GradeZeroInterpolatingElement.main` in SymplecticGSp4/ConductorAtMapInjectiveCoeff.lean. The proof of `of_four_alt` in [HVCore.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/HVCore.lean#L18) applies the window theorem at the literal exponent `401`, and the file also holds the unrelated theorem `modU_of_printsH`. We have not unfolded the predicates `Chr.V'`, `ThmBab` and `ThmBcFree`.
