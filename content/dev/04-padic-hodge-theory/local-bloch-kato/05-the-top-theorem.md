---
title: The top theorem
decls:
  - GlobalTheory.TopBridge.twistedLatticeCohomology_theoremTOP
  - GlobalTheory.T.blochKatoTop_of_localTateDuality_eulerChar
  - GlobalTheory.TopClosing.blochKatoTop_of_localTateDuality_eulerChar_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The top theorem

This section proves the exact local conditions of Section 1 at every prime, for the local data of the series. It first proves them from a list of admitted local statements, by the results of Sections 1 to 4. Then it proves the admitted statements from local Tate duality and the local Euler characteristic formula. The result is used in [the congruence bound along a family](/entry/nlink-e-main-alt-alt/) of the third-place series.

Let $D$ be the data of the series. For each prime $\ell$ they give period data at $\ell$ with $A_{\inf}$-data and a tie to a model, as in Section 1. *Local data* over $D$ are, at each prime $\ell$, Wach data $H_\ell$, Fontaine data $F_\ell$ for $H_\ell$, and comparison data $C_\ell$ for $F_\ell$.

**Definition 7.5.1 (Local top theorem).** The *local top theorem* for $D$, $H$ and $F$ is the statement: for every prime $\ell$, all finite extensions $K$ and $L$ of $\mathbb{Q}_\ell$ with $(K, L)$ in Case A, and every irreducible $\lambda \in \mathcal{O}$, the top core of Section 1 holds for the embeddings $\tau_i$ of the Wach data $H_\ell$ at $(K, L)$, the element $\lambda$ and the inertia group $I_K$.

**Definition 7.5.2 (Admitted local statements).** The *admitted local statements* for $D$, $H$, $F$ and $C$ are the conjunction of 24 statements. Statements 1 to 15 and 23, 24 are properties of the Wach data, the Fontaine data and the comparison data; statements 16 and 17 are properties of Herr complexes of Wach modules. Statement 18 is the pair (local Tate duality, local Euler characteristic formula) of Section 4. Statement 19 is the Bloch-Kato formula of Section 4 for all $(K, L)$ in Case A, with its two extra clauses. Statement 20 asks for crystalline characters with given jumps and says that unramified twists keep a crystalline representation crystalline with the same jumps. Statement 21 is a statement on Sen operators of Wach lattices, and statement 22 a calculus of crystalline characters and their inverses. We do not unfold statements 1 to 17 and 20 to 24.

**Theorem 7.5.3 (The top theorem).** Let $D$ be the data of the series and $H$, $F$, $C$ local data over $D$. If the admitted local statements hold, then the local top theorem holds for $D$, $H$ and $F$.

Lean: `GlobalTheory.TopBridge.twistedLatticeCohomology_theoremTOP`.

*Proof.* Fix $\ell$, $(K, L)$ in Case A and an irreducible $\lambda$. The tie of $D$ at $\ell$ gives the crystalline calculus of Section 3 for every local situation at $\ell$.

*Reality.* Let $S$ be a local situation at $\ell$. By [Theorem 7.3.6](/entry/real-d/), $S$ is presented. The admitted local statements give the used properties of the Wach data of $S$; these Wach data are those of $H_\ell$ at the fields of $S$, which are in Case A by the standing hypotheses. So $S$ is real by [Theorem 7.3.8](/entry/real-of-presented/).

*The three statements at one prime.* The statement at one prime is [Theorem 7.4.8](/entry/stmt-at-of-real/), applied to statement 18 (Tate duality and the Euler characteristic), the tie, the reality of all local situations at $\ell$, and statement 19 (the Bloch-Kato formula). The statement on twisted characters follows from the crystalline calculus and reality. Fix $2 \le c \le t$. The crystalline calculus gives the basic facts of Section 4 for $\mathcal{O}(\chi_c)$. Reality at a residue field and the bound of the model theory show that no admissible class in $\mathrm{adm}(\mathcal{O}(\chi_c), \mathcal{O}/\lambda)$ is independent modulo $\lambda$, that is, every such class is 0. For a finite $X \ne 0$ we use induction on $\# X$. Choose an injection $f : \mathcal{O}/\lambda \to X$. An admissible class at $X$ maps to an admissible class at $X/f(\mathcal{O}/\lambda)$, which is 0 by induction. So it comes from a class at $\mathcal{O}/\lambda$, since $\mathcal{O}(\chi_c)$ is flat and the sequence of coefficients is exact. That class is admissible, since $f$ is injective, so it is 0. Thus $\mathrm{adm}(\mathcal{O}(\chi_c), X) = 0$ for every finite $X$. The statement on the first character follows in the same way. The basic facts hold for $\mathcal{O}(\chi_1)$, reality bounds the number of admissible classes at $\mathcal{O}/\lambda$ that are independent modulo $\lambda$ by 1, the unramified classes are admissible, and these facts give $\mathrm{adm}(\mathcal{O}(\chi_1), X) = H^1_{\mathrm{ur}}(X)$.

*Conclusion.* [The exact local conditions](/entry/exact-local-conditions-top-core/), applied to the tie, the Wach data and the three statements, give the top core at $(K, L)$ and $\lambda$. $\square$

Now we state the published input of the second theorem. Let $K$ be a finite extension of $\mathbb{Q}_\ell$ and $V$ a finite-dimensional representation of $G_K$ over $\mathbb{Q}_\ell$. Put $D_{\mathrm{dR}}(V) = (V \otimes B_{\mathrm{dR}})^{G_K}$; $V$ is *de Rham* if $\dim_K D_{\mathrm{dR}}(V) = \dim_{\mathbb{Q}_\ell} V$.

**Theorem 7.5.4 (Bloch-Kato).** Let $V$ be a de Rham representation of $G_K$ over $\mathbb{Q}_\ell$. Then
$$\dim_{\mathbb{Q}_\ell} H^1_f(K, V) = \dim_{\mathbb{Q}_\ell} H^0(K, V) + \dim_{\mathbb{Q}_\ell} D_{\mathrm{dR}}(V)/\mathrm{Fil}^0 D_{\mathrm{dR}}(V).$$
If $V'$ is dual to $V(1)$ for a pairing $V \times V' \to \mathbb{Q}_\ell(1)$, then $H^1_f(K, V)$ and $H^1_f(K, V')$ are exact annihilators of each other under the cup product into $H^2(K, \mathbb{Q}_\ell(1))$.

See Bloch and Kato, *L-functions and Tamagawa numbers of motives*, in *The Grothendieck Festschrift*, Vol. I, 1990, Proposition 3.8 and Corollary 3.8.4.

**Remark 7.5.5.** The Lean form asks the period data to be tied to a model, states the duality on the level of cocycles, and adds an integral form of the duality for lattices, with the finite parts of divisible cocycles. We state that form only in these words, since it is not used.

**Theorem 7.5.6 (Exact local conditions at every prime).** Assume the theorem of Bloch and Kato, local Tate duality and the local Euler characteristic formula. Let $D$ be the data of the series and $H$, $F$, $C$ local data over $D$. Then the local top theorem holds for $D$, $H$ and $F$.

Lean: `GlobalTheory.T.blochKatoTop_of_localTateDuality_eulerChar` (also `GlobalTheory.TopClosing.blochKatoTop_of_localTateDuality_eulerChar_alt`).

*Proof.* We prove the admitted local statements and apply [the top theorem](/entry/twisted-lattice-cohomology-theorem-top/). A theorem on Wach lattices for the local data gives 17 statements. Fifteen of them are statements 1 to 15, one is not used, and the last one gives statements 23 and 24. Statement 16 comes from the theory of Herr complexes: the class map of Herr complexes is injective and bijective on norms, the invariants statement follows from the Fontaine equivalence and decompletion, and the Fontaine functor is fully faithful and exact with an operator $\psi$. Statement 17 comes from the existence of lattices for powers in étale submodules and an extension rule. Statement 18 is the pair of hypotheses. Statement 19 is proved from the tie: the Bloch-Kato formula for crystalline representations over $L$ in Case A holds through the tie, the saturation clause holds since $H^1_f$ of $V$ is an $L$-subspace, and finite cocycles of the trivial representation are unramified by a lemma on the tie. Statement 20 is the existence of crystalline characters with given jumps and the rule for unramified twists, statement 21 follows from statements 2, 4, 5, 9 and 11, and statement 22 is the calculus of crystalline characters. $\square$

**Remark 7.5.7 (Formalization).** The hypothesis of Bloch and Kato is never used ([BlochKatoTopOfLocalTateDualityEulerChar.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BlochKatoTopOfLocalTateDualityEulerChar.lean#L28) introduces it as `_`); statement 19 is proved from the tie. So the only inputs from the literature in this chain are Tate duality and the Euler characteristic. The comparison data $C$ are used in the proof but do not appear in the conclusion. Statement 18 does not depend on $D$, although it is written as a statement about $D$. The second Lean name is a wrapper that sets `maxHeartbeats` to 1000000 for a one-line proof.
