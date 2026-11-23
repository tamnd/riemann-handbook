---
title: The local count and the link along families
decls:
  - GlobalTheory.Pass.LocDual.main
  - GlobalTheory.T.localCountDualLifting_proof
  - GlobalTheory.LinkFam.main
  - GlobalTheory.T.linkN_along_family_of_localBounds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local count and the link along families

This last section proves two statements that the assembly volume uses. The first is a local count. At a place $w$ of degree one over a prime $\ell$, the length of the span of the cut cocycles modulo the finite classes is at most $2ke$ times a fixed length, where $k$ is the rank of the twisted representation and $e$ is the lifting exponent of the dual family. It is one of the steps of [the theorem on the steps without a cut](/entry/steps-no-cut-of-artin-alt/). The second statement takes the local conclusions along a family of data and gives the link bound of [the link theorem](/entry/link-n-of-tw-good-galois-preconditions/). Both proofs combine given theorems with a short monotonicity lemma.

We work with a global datum $D$ of the assembly volume. It gives a set of local indices $i$, each with a prime $\ell_i$, a ring $\mathcal{O}_i$ and a field $K_i$ of fractions, a family $r = (r_x)$ of representations $G_E \to \mathrm{GL}_{n_V}(\mathcal{O}_i)$ indexed by a set $X_i$, the twists $r^{\mathrm{tw}}_x$ and the duals $r^{\vee}_x$ of the members of the family, and for each place $w$ of the host field over $\ell_i$ a local field $K_w$, its Galois group $G_w$, a coefficient field $\Lambda_w$ with ring of integers $\mathcal{O}_w$, and period data $\mathrm{PD}_w$ for $G_w$. We do not unfold the datum $D$, the twists or the duals.

### The local count

**Definition 7.27.1 (Length modulo a submodule).** Let $O$ be a commutative ring, $M$ an $O$-module and $S, H$ submodules of $M$. The *length of $S$ modulo $H$* is
$$\lambda(S, H) = \mathrm{length}_O \bigl( (S + H)/H \bigr) \in \mathbb{N} \cup \{\infty\}.$$

**Definition 7.27.2 (The pushout span).** Let $X$ and $U$ be representations of $G_w$ over $\Lambda_w$ and let $T$ be an $\mathcal{O}_w$-lattice in $U$. The *pushout span* $\mathrm{Push}(X, U, T)$ is the $\mathcal{O}_w$-submodule of the maps $G_w \to U/T$ spanned by the maps $\phi_* y$, where $Y$ is a lattice in $X$, $\phi : Y \to U/T$ is an $\mathcal{O}_w$-linear map compatible with $G_w$, and $y$ is a cocycle with values in $Y$ whose class is finite for $\mathrm{PD}_w$. We do not unfold the compatibility condition or the finite cocycles.

For a continuous $M : G_E \to M_k(\mathcal{O}_i)$ let $U_M$ be the local representation of $G_w$ on $\Lambda_w^k$ given by $M$ and let $T_M$ be its standard lattice. Let $H^1_f(T_M)$ be the submodule of the maps $G_w \to U_M/T_M$ given by the finite classes, and let $\lambda_w \in \mathbb{N} \cup \{\infty\}$ be the length attached to $\mathrm{PD}_w$ and $\mathcal{O}_w$. For a subset $X_s \subseteq X_i$, the set $\mathrm{Cut}(r, X_s, M)$ of *cut cocycles* is a set of maps $G_w \to U_M/T_M$ built from finitely many members $r_x$ with $x \in X_s$. We do not unfold $H^1_f$, $\lambda_w$ or the cut cocycles.

**Definition 7.27.3 (The local bound).** For an integer $b \ge 0$, the *local bound* $\mathrm{LB}(i, w, r, X_s, M, b)$ is the inequality
$$\lambda\bigl( \mathrm{span}_{\mathcal{O}_w} \mathrm{Cut}(r, X_s, M), \, H^1_f(T_M) \bigr) \le b \, \lambda_w.$$

**Lemma 7.27.4 (Monotonicity).** Let $O$ be a commutative ring, $M$ an $O$-module and $S \subseteq S'$ and $H$ submodules of $M$. Then $\lambda(S, H) \le \lambda(S', H)$.

*Proof.* Since $S \subseteq S'$, we have $S + H \subseteq S' + H$. The inclusion sends $H$ into $H$, so it gives an $O$-linear map $f : (S + H)/H \to (S' + H)/H$. Let $z = x + H$ be in the kernel of $f$, with $x \in S + H$. Then $x \in H$, so $z = 0$. Thus $f$ is injective, and the length of a module is at most the length of a module into which it injects. $\square$

The proof of the local count uses six given theorems. The hypotheses of the theorem below are named in them: *Fontaine* is a hypothesis on the period data at the places over the primes $\ell_i$, *PotDR* is a potentially de Rham condition on the local data of $D$, *admBK* is a hypothesis of $D$ on Breuil-Kisin modules, *GoodR* is a goodness condition on the family $r$, $\mathrm{PotFam}(n)$ says that there are a finite normal extension $K'$ of $K_w$ and a Frobenius stable set $\Sigma$ of at most $n$ characters of inertia, with $1 \in \Sigma$, such that each twist $r^{\mathrm{tw}}_x$ with $x \in X_s$ is potentially crystalline over $K'$ with inertia acting through $\Sigma$, $\mathrm{LiftFam}(e)$ says that surjective lattice maps between sums of the duals $r^{\vee}_x$ for $x \in X_s$ lift with the exponent $e$, and $\mathrm{SubTw}(M)$ says that $M$ is continuous and $M \otimes K_i$ embeds, compatibly with $G_E$, into one twist $r^{\mathrm{tw}}_x \otimes K_i$ with $x \in X_s$. We do not unfold these conditions beyond this description.

**Theorem 7.27.5 (Finite reduction).** Let $S$ be a subset of $M$, $H$ a submodule and $b \in \mathbb{N} \cup \{\infty\}$. If $\lambda(\mathrm{span}\, F, H) \le b$ for every finite $F \subseteq S$, then $\lambda(\mathrm{span}\, S, H) \le b$.

**Theorem 7.27.6 (Cut cocycles in a pushout span).** Assume Fontaine, GoodR and $\mathrm{PotFam}(n)$, and let $M$ satisfy $\mathrm{SubTw}(M)$. For every finite $F \subseteq \mathrm{Cut}(r, X_s, M)$ there is a summand $X$ of the localized twists $r^{\mathrm{tw}}_x$, $x \in X_s$, with $\mathrm{span}\, F \subseteq \mathrm{Push}(X, U_M, T_M)$.

**Theorem 7.27.7 (Duals of summands).** Assume Fontaine, PotDR, GoodR and $\mathrm{PotFam}(n)$. Every such summand $X$ is de Rham, and there are a representation $X'$ and a pairing $P_X : X \times X' \to \Lambda_w$ that is a duality for $\mathrm{PD}_w$, with $X'$ a subfamily of the localized duals $r^{\vee}_x$, $x \in X_s$.

**Theorem 7.27.8 (The crystalline potential family).** Assume Fontaine, PotDR, admBK, GoodR, $[K_w : \mathbb{Q}_{\ell_i}] = 1$ and $\mathrm{PotFam}(n)$, and let $M$ satisfy $\mathrm{SubTw}(M)$. Then $U_M$ is de Rham, and there are a representation $U'$, a subfamily of the localized duals, a pairing $P_U : U_M \times U' \to \Lambda_w$ and a lattice $T'$ in $U'$ such that $P_U$ makes $T'$ a dual lattice of $T_M$ and
$$\mathrm{rank}_{\mathcal{O}_w} H^1_f(T') + \mathrm{rank}_{\mathcal{O}_w} T_M \le 2k.$$

**Theorem 7.27.9 (Lifts from a family).** If a family of matrix representations has $\mathrm{LiftFam}(e)$ and $A$ and $A'$ are subfamilies of it, then $\mathrm{LiftAll}(A, A', e)$: every surjective lattice map between subsums of $A$ and $A'$ lifts with the exponent $e$.

**Theorem 7.27.10 (The pushout bound).** Let $V, X, U, X', U'$ be representations of $G_w$, $\chi$ a character, $P_X$ and $P_U$ pairings, $T$ a lattice in $U$, $T'$ a lattice in $U'$ and $e \ge 0$. Assume the *hypothesis* $\mathrm{Hyp}$: $X$ is the twist of $V$ by $\chi^{-1}$, $U$ is de Rham, $P_X$ is a duality, $P_U$ makes $T'$ a dual lattice of $T$, and either $\mathrm{LiftAll}(X, U, e)$, or $X$ is de Rham and $\mathrm{LiftAll}(X', U', e)$. Then there are $m, \kappa \in \mathbb{N}$ with $\lambda(\mathrm{Push}(X, U, T), H^1_f(T)) = m$, $\lambda_w = \kappa$ and
$$m \le e \, \bigl( \mathrm{rank}\, H^1_f(T') + \mathrm{rank}\, T \bigr) \, \kappa.$$

The local pushout proposition for $D$ is the pair of this pushout bound and one more statement, the arc theorem, at all local period data of $D$.

**Theorem 7.27.11 (Local count for duals).** Let $D$ satisfy the local pushout proposition, admBK, Fontaine and PotDR. Let $i$ be a local index, $r$ a family with GoodR, $X_s \subseteq X_i$ and $w$ a place over $\ell_i$ with $[K_w : \mathbb{Q}_{\ell_i}] = 1$. Let $n, e \ge 0$ with $\mathrm{PotFam}(n)$ and $\mathrm{LiftFam}(e)$, and let $M : G_E \to M_k(\mathcal{O}_i)$ satisfy $\mathrm{SubTw}(M)$. Then $\mathrm{LB}(i, w, r, X_s, M, 2ke)$ holds.

Lean: `GlobalTheory.Pass.LocDual.main` (also `GlobalTheory.T.localCountDualLifting_proof`, a second name).

*Proof.* By the finite reduction it is enough to show $\lambda(\mathrm{span}\, F, H^1_f(T_M)) \le 2ke \, \lambda_w$ for a finite $F \subseteq \mathrm{Cut}(r, X_s, M)$. Fix such an $F$.

Step 1. The theorem on cut cocycles gives a summand $X$ of the twists with $\mathrm{span}\, F \subseteq \mathrm{Push}(X, U_M, T_M)$.

Step 2. The theorem on duals of summands gives that $X$ is de Rham, and gives $X'$ and a duality $P_X$ with $X'$ a subfamily of the duals.

Step 3. The theorem on the crystalline potential family uses the degree $[K_w : \mathbb{Q}_{\ell_i}] = 1$ and admBK. It gives that $U_M$ is de Rham, and gives $U'$, $P_U$ and $T'$ with $\mathrm{rank}\, H^1_f(T') + \mathrm{rank}\, T_M \le 2k$, with $U'$ a subfamily of the duals.

Step 4. The duals have $\mathrm{LiftFam}(e)$, and $X'$ and $U'$ are subfamilies of them, so the theorem on lifts from a family gives $\mathrm{LiftAll}(X', U', e)$.

Step 5. Take $V = X$ and $\chi = 1$. Then $X$ is the twist of $V$ by $\chi^{-1} = 1$, with the identity map as witness. With the second branch of the alternative, Steps 2 to 4 give $\mathrm{Hyp}$ for $(X, X, U_M, X', U', 1, P_X, P_U, T_M, T', e)$.

Step 6. The pushout bound gives $m, \kappa$ with $\lambda(\mathrm{Push}(X, U_M, T_M), H^1_f(T_M)) = m$, $\lambda_w = \kappa$ and $m \le e(\mathrm{rank}\, H^1_f(T') + \mathrm{rank}\, T_M)\kappa$. By Step 3, $m \le e \cdot 2k \cdot \kappa = 2ke\kappa$.

Step 7. By Step 1 and the monotonicity lemma,
$$\begin{aligned} \lambda\bigl(\mathrm{span}\, F, H^1_f(T_M)\bigr) &\le \lambda\bigl(\mathrm{Push}(X, U_M, T_M), H^1_f(T_M)\bigr) \\ &= m \le 2ke \, \kappa = 2ke \, \lambda_w. \end{aligned}$$
$\square$

The bound does not depend on $n$. Only the second branch of $\mathrm{Hyp}$ is used, since the lifting condition is given for the duals.

### The link along a family

A *family* $\mathcal{F}$ with parameter $\varepsilon$ gives, for each real $x$, an index set $I_x$ and, for $i \in I_x$, a global datum $D(x, i)$ with size data $L(x, i)$, and, for $x > x_1$, a parameter choice $P(x, i)$. A datum $D$ is *odd* if its Tate-Shafarevich condition $\mathrm{ShaFinOdd}(D)$ holds. We do not unfold families, size data, parameter choices or this condition.

For size data $L$ of $D$, parameters $P$, a hub datum $X$ and a constant $C$, the *local bounds conclusion* $\mathrm{Concl}(L, P, X, C)$ is a list of fifteen conditions on $L$, $P$, $X$ and $C$, the first of which is $C \ge 0$. The *admissible statements* $\mathrm{AdmT}(L, t, C, P)$ for a table $t$ are a list of seventeen conditions. We do not unfold either list.

**Definition 7.27.12 (Family conditions).** Let $\mathcal{F}$ be a family.

1. $\mathrm{ConclF}(\mathcal{F})$: there are $C$ and $x_0$ such that for all $x \ge x_0$ with $x > x_1$ and all $i \in I_x$ with $D(x, i)$ odd, there is a hub datum $X$ with $\mathrm{Concl}(L(x, i), P(x, i), X, C)$.
2. $\mathrm{AdmF}(\mathcal{F})$: there are $C$ and $x_0$ such that for all $x \ge x_0$ with $x > x_1$ and all $i \in I_x$, if $D(x, i)$ is odd, then there is a table $t$ with $\mathrm{AdmT}(L(x, i), t, C, P(x, i))$.
3. $\mathrm{LinkN}(\mathcal{F})$: there are $C$ and $x_0$ such that for all $x \ge x_0$, all $i \in I_x$ with $D = D(x, i)$ odd and all lifts $j$ of $D$, if the terms $v(l)$ of $D$ are summable, then
$$\begin{aligned} \eta(L, j) \le d_0(j) \Bigl( & C \bigl( f m b \, \Lambda^2 + (\log x)^2 N_c \bigr) \\ & + \textstyle\sum_l v(l) \Bigr), \end{aligned}$$
where $L = L(x, i)$, and $\eta$, $d_0$, $f$, $m$, $b$, $\Lambda$, $N_c$ and $v$ are read from $D$ and $L$. We do not unfold them.

**Theorem 7.27.13 (Admissible statements from local bounds).** If $\mathrm{Concl}(L, P, X, C)$ holds, then there is a table $t$ with $\mathrm{AdmT}(L, t, C, P)$.

**Theorem 7.27.14 (The family statement).** For every family $\mathcal{F}$, $\mathrm{AdmF}(\mathcal{F})$ implies the orbit valuation bound for $\mathcal{F}$, and this bound gives $\mathrm{LinkN}(\mathcal{F})$.

The first half of this theorem has no hypothesis beyond $\mathrm{AdmF}$; it is [the unconditional family statement](/entry/stmt-f-holds/).

**Theorem 7.27.15 (Link along a family).** Let $\mathcal{F}$ be a family with $\mathrm{ConclF}(\mathcal{F})$. Then $\mathrm{LinkN}(\mathcal{F})$ holds.

Lean: `GlobalTheory.LinkFam.main` (also `GlobalTheory.T.linkN_along_family_of_localBounds`, a second name).

*Proof.* Take $C$ and $x_0$ from $\mathrm{ConclF}(\mathcal{F})$. Let $x \ge x_0$ with $x > x_1$, let $i \in I_x$ and assume that $D(x, i)$ is odd. Then there is a hub datum $X$ with $\mathrm{Concl}(L(x, i), P(x, i), X, C)$, and the theorem on admissible statements gives a table $t$ with $\mathrm{AdmT}(L(x, i), t, C, P(x, i))$. So $C$ and $x_0$ show $\mathrm{AdmF}(\mathcal{F})$. The theorem on the family statement then gives $\mathrm{LinkN}(\mathcal{F})$. $\square$ The constant of $\mathrm{LinkN}$ is a new constant that depends on $C$.

**Remark 7.27.16 (Formalization).** The inputs of the local count are `GlobalTheory.T.lengthModulo_span_le_of_forall_finset`, `GlobalTheory.T.localCocycles_mem_span_pushout_summandLattice`, `GlobalTheory.T.potential_family_summand_restriction`, `GlobalTheory.T.crystalline_potential_family`, `GlobalTheory.T.liftAll_subSums_of_liftFamily_matrixFamily` and the second part of the hypothesis `LocalPushoutProposition`, that is `BlochKatoDuality.Conclusion2`, an instance of `PushoutSpanLengthBound` ([BlochKatoDuality.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BlochKatoDuality.lean#L95)). The inputs of the link are `GlobalTheory.T.admittedStatements_of_localBoundsConclusion_alt`, `Formalism.MainNotions.TwistedPlaces.stmtF_holds` and `Formalism.MainNotions.N.linkN_of`. We read their statements, not their proofs. The monotonicity lemma is the helper `T2` in the same file ([LocalCountDualLiftingProof.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalCountDualLiftingProof.lean#L13)); the length $\lambda$ is `lenMod`, the pushout span is `spanPush`, the local bound is `LocBoundP`, and the statement of the local count is the proposition `StepLocDual`. The proof of the local count sets `maxHeartbeats` to 2000000 and `synthInstance.maxHeartbeats` to 400000 ([LocalCountDualLiftingProof.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalCountDualLiftingProof.lean#L28)). The first part of `LocalPushoutProposition`, the arc theorem `Conclusion1`, is not used: only `hLOC.2` is called ([LocalCountDualLiftingProof.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalCountDualLiftingProof.lean#L43)). The hypothesis $\mathrm{Hyp}$ is built with `Or.inr`, and the twist in Step 5 is `LinearEquiv.refl` ([LocalCountDualLiftingProof.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalCountDualLiftingProof.lean#L39)). The wrappers of the inputs of the local count set `maxHeartbeats 1000000` twice, at lines 6 and 8 ([CrystallinePotentialFamilyStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallinePotentialFamilyStatement.lean#L6)). In the link, the family statement `stmtF_holds` ([ExportBoundOfAdmissible.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ExportBoundOfAdmissible.lean#L1160)) is proved with no hypothesis, through `stmtU_holds` with the constant $2000(|C| + 1)^3$ ([ExportBoundOfAdmissible.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ExportBoundOfAdmissible.lean#L1141)), so the hypothesis `KudlaFamilyStatement` of `linkN_of` costs nothing ([LinkNAlongFamilyOfLocalBounds.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LinkNAlongFamilyOfLocalBounds.lean#L17)). The proof of the link does not look at the fields of `Concl` or `AdmT`.

## Notes and references

This chapter feeds the assembly volume in four places. The sections on Breuil-Kisin modules build up to [the lifting along a surjection of good lattices](/entry/lift-f-of-is-good/), which [Theorem T at each prime](/entry/theorem-tclosing-main/) uses; Theorem T in turn gives local inputs for the unitary hypotheses. The local count of this section is one of the steps of [the theorem on the steps without a cut](/entry/steps-no-cut-of-artin-alt/), and the link along families gives [the link theorem](/entry/link-n-of-tw-good-galois-preconditions/). The main difference from the classical sources below is that each bound here is explicit in the Hodge-Tate jumps, the ramification index and the lifting exponents.

- The period rings $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$: J.-M. Fontaine, *Le corps des périodes p-adiques*, Astérisque 223 (1994), Exposé II.
- Semistable and crystalline representations: J.-M. Fontaine, *Représentations p-adiques semi-stables*, Astérisque 223 (1994), Exposé VIII.
- Breuil-Kisin modules and their comparison with crystalline representations: M. Kisin, *Crystalline representations and F-crystals*, in *Algebraic Geometry and Number Theory*, Progr. Math. 253, Birkhäuser, 2006.
- The groups $H^1_f$ of finite classes: S. Bloch and K. Kato, *L-functions and Tamagawa numbers of motives*, in *The Grothendieck Festschrift* I, Progr. Math. 86, Birkhäuser, 1990, §3.
- The Galois cohomology of $p$-adic fields: J.-P. Serre, *Cohomologie galoisienne*, Lecture Notes in Math. 5, Springer, Chapter II, §5.
- The characters of tame inertia: J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. 15 (1972), §1.
- Modules of finite length: M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969, Chapter 6.
