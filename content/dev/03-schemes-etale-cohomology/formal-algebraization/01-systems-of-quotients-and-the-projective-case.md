---
title: Systems of quotients and the projective case
decls:
  - GlobalTheory.CompanionTheory.GE.exists_sub_of_ample
  - GlobalTheory.CompanionTheory.GE.statement_open_projective
  - GlobalTheory.T.formal_existence_projective_open
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Systems of quotients and the projective case

This section starts the proof of Grothendieck's existence theorem for closed subschemes. We state the theorem in a form for coherent sheaves: a compatible system of quotients of the reductions of a coherent sheaf modulo the powers of an ideal comes from one quotient of the sheaf, if the support is proper. This section proves that form on an open subscheme of a projective scheme. The proof uses an ample line bundle and the sections of its large powers. Section 2 transfers the result along a proper map, and Section 3 then proves the general case by Noetherian induction.

Throughout Sections 1 to 3, $A$ is a Noetherian ring and $I \subseteq A$ is an ideal. We say that $A$ is *$I$-adically complete* if the map $A \to \varprojlim_e A/I^{e+1}$ is bijective, so $A$ is separated and complete ([completion](/learn/commutative-algebra/#completion)). Let $X$ be a scheme over $\operatorname{Spec} A$. For an $\mathcal{O}_X$-module $E$ and $n \geq 0$ we write $I^n E$ for the image of $I^n \otimes_A E \to E$. For a quasi-coherent ideal sheaf $J \subseteq \mathcal{O}_X$ we write $V(J)$ for the closed subscheme that it defines ([schemes](/learn/geometry/#schemes-and-varieties)).

**Definition 7.1.1 (Closed system).** Let $E$ be an $\mathcal{O}_X$-module. A *closed system* in $E$ is a sequence $(S_e)_{e \geq 0}$ of quasi-coherent submodules of $E$ such that, for each $e \geq 0$,
$$I^{e+1} E \subseteq S_e, \qquad S_e = S_{e+1} + I^{e+1} E.$$

Let $X_e = X \times_A \operatorname{Spec} A/I^{e+1}$ be the $e$-th thickening. The first condition says that $E/S_e$ is a module on $X_e$. The second says that $(E/S_{e+1}) / I^{e+1} (E/S_{e+1}) = E/S_e$. So a closed system is the same as a compatible system of quotients $E_e \to Q_e$ of the reductions $E_e = E/I^{e+1}E$, with $Q_{e+1} \otimes A/I^{e+1} = Q_e$. If $E$ is coherent, this is a coherent quotient of the formal completion of $E$ along $X_0$ ([formal functions](/learn/commutative-algebra/#formal-functions-and-grothendiecks-existence-theorem)).

**Definition 7.1.2 (Proper support, killed, algebraizable).** Let $E$ be an $\mathcal{O}_X$-module and $S \subseteq E$ a submodule.

1. $S$ has *proper support* if there is a quasi-coherent ideal sheaf $T \subseteq \mathcal{O}_X$ such that $V(T) \to \operatorname{Spec} A$ is proper and the support of $E/S$ is in $V(T)$.
2. Let $J \subseteq \mathcal{O}_X$ be an ideal sheaf. $S$ is *killed by $J$* if $a x \in S(U)$ for each affine open $U$, each $a \in J(U)$ and each $x \in E(U)$. So $J E \subseteq S$, and $E/S$ is a module on $V(J)$.
3. A closed system $(S_e)$ in $E$ is *algebraizable* if there is a quasi-coherent submodule $B \subseteq E$ with proper support such that $B + I^{e+1} E = S_e$ for each $e \geq 0$.

If $(S_e)$ is algebraizable by $B$, then $Q = E/B$ is a quotient of $E$ with proper support, and $Q / I^{e+1} Q = E/S_e$ for each $e$. So $Q$ is the algebraic object that the formal system comes from.

**Definition 7.1.3 (The statement for an ideal sheaf).** Let $J \subseteq \mathcal{O}_X$ be a quasi-coherent ideal sheaf. We say that $\mathrm{St}(J)$ *holds on* $X$ if the following is true. For each coherent $\mathcal{O}_X$-module $E$ and each closed system $(S_e)$ in $E$ such that each $S_e$ is killed by $J$ and $S_0$ has proper support, the system $(S_e)$ is algebraizable.

For $J = 0$ the condition "killed by $J$" is empty, so $\mathrm{St}(0)$ is the full statement. For $J = \mathcal{O}_X$ each $S_e$ is equal to $E$, and $B = E$ algebraizes the system. The proof of the general case in Section 3 is a descending induction on $J$, from $\mathcal{O}_X$ to $0$.

For a line bundle $H$ on $X$ and $n \in \mathbb{Z}$ we write $P(n) = P \otimes H^{\otimes n}$. For a submodule $S \subseteq P$ we write $\Gamma_n(S)$ for the image of $\Gamma(X, S(n)) \to \Gamma(X, P(n))$. We use [ample line bundles](/learn/positivity-resolution/#ample-nef-and-big-line-bundles) and [coherent cohomology](/learn/commutative-algebra/#coherent-cohomology).

**Theorem 7.1.4 (Algebraization with an ample line bundle).** Let $A$ be Noetherian and $I$-adically complete, and let $X$ be proper over $\operatorname{Spec} A$. Let $H$ be an ample line bundle on $X$, let $P$ be a coherent $\mathcal{O}_X$-module and let $(S_e)$ be a closed system in $P$. Then there is a quasi-coherent submodule $B \subseteq P$ with $B + I^{e+1} P = S_e$ for each $e \geq 0$.

Lean: `GlobalTheory.CompanionTheory.GE.exists_sub_of_ample`.

The theorem does not claim that $B$ has proper support. In the application below the support is controlled by a separate argument.

*Proof.* The space $X$ is locally Noetherian, since it is of finite type over the Noetherian ring $A$, and it is quasi-compact. So $X$ is Noetherian. We take the following three facts as given. They are the steps of the proof of the projective case in EGA III_1, Théorème 5.1.4, and they come from the fact that the graded ring $\bigoplus_e I^e / I^{e+1}$ is Noetherian, which gives a uniform vanishing of $H^1$ and a uniform generation by sections for the graded pieces of the system.

1. *Approximation.* There is $n_1 \in \mathbb{Z}$ such that, for each $n \geq n_1$, each $e \geq 0$ and each $x \in \Gamma_n(S_e)$, there is $y \in \Gamma_n(S_{e+1})$ with $x - y \in \Gamma_n(I^{e+1} P)$.
2. *Limit.* Let $n$ be such that the conclusion of the first fact holds. Then there is a set $W_n \subseteq \Gamma(X, P(n))$ with $W_n \subseteq \Gamma_n(S_e)$ for each $e$, such that for each $e$ and each $x \in \Gamma_n(S_e)$ there is $b \in W_n$ with $x - b \in \Gamma_n(I^{e+1} P)$.
3. *Generation.* Let $n_1 \in \mathbb{Z}$ and let $W_n \subseteq \Gamma(X, P(n))$ be sets with $W_n \subseteq \Gamma_n(S_e)$ for all $n$ and $e$, and with the approximation property of the second fact for $n \geq n_1$. Then there is a quasi-coherent $B \subseteq P$ with $B + I^{e+1} P = S_e$ for each $e$.

The second fact uses the completeness of $A$: the module $\Gamma(X, P(n))$ is finite over $A$, so it is $I$-adically complete, and the corrections of the first fact converge. In the third fact $B$ is built from the twisted sections in the sets $W_n$ for $n \geq n_1$. This is where ampleness enters, since the sections of large twists generate.

Now take $n_1$ from the first fact. For $n \geq n_1$ let $W_n$ be the set of the second fact, and for $n < n_1$ let $W_n = \emptyset$. The empty set is contained in each $\Gamma_n(S_e)$, and the approximation property is only required for $n \geq n_1$. So the sets $W_n$ satisfy the hypotheses of the third fact, and it gives $B$. $\square$

**Theorem 7.1.5 (Existence on an open subscheme of a projective scheme).** Let $A$ be Noetherian and $I$-adically complete. Let $N \geq 0$, let $i : Y \to \mathbb{P}^N_A$ be a closed immersion and let $O \subseteq Y$ be open. View $O$ as a scheme over $\operatorname{Spec} A$ through $O \to Y \to \mathbb{P}^N_A \to \operatorname{Spec} A$. Then $\mathrm{St}(0)$ holds on $O$.

Lean: `GlobalTheory.CompanionTheory.GE.statement_open_projective` (also `GlobalTheory.T.formal_existence_projective_open`, a second name).

*Proof.* The projective space $\mathbb{P}^N_A$ is proper over $A$, and so is the closed subscheme $Y$. So $Y$ is Noetherian. The line bundle $\mathcal{O}(1)$ is ample on $\mathbb{P}^N_A$, and $i$ is affine, so $H = i^* \mathcal{O}(1)$ is ample on $Y$.

Let $E$ be a coherent module on $O$ and $(S_e)$ a closed system in $E$ such that $S_0$ has proper support, with ideal sheaf $T$. The condition that each $S_e$ is killed by the zero ideal is empty, and we do not use it. We use four inputs, which we take as given.

1. Since $H$ is ample, there is a coherent module $P$ on $Y$ and a surjection $f : P|_O \to E$.
2. From $f$ and the support condition on $S_0$ there is a closed system $(\bar S_e)$ in $P$ that is compatible with $(S_e)$ along $f$. The input also gives a closedness fact for the support, which is used in the fourth step.
3. If $\bar B \subseteq P$ is quasi-coherent with $\bar B + I^{e+1} P = \bar S_e$ for all $e$, then there is a quasi-coherent $B \subseteq E$ with $B + I^{e+1} E = S_e$ for all $e$, and $B$ is related to $\bar B$ along $f$.
4. In the situation of the third input, $B$ has proper support.

The theorem on ample line bundles above, applied to $Y$, $H$, $P$ and $(\bar S_e)$, gives $\bar B$. The third input gives $B$, and the fourth input shows that $B$ has proper support. So $B$ algebraizes $(S_e)$. $\square$

This theorem is the base case of the proper pushforward step in Section 2. There the scheme $O$ is an open subscheme of a projective scheme that maps properly onto an integral closed subscheme, by Chow's lemma.

**Remark 7.1.6 (Formalization).** The definitions of closed systems, proper support, the killing condition and the statement $\mathrm{St}(J)$ are in [PowSubSuccLe.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PowSubSuccLe.lean#L17). The two theorems are in [FormalExistenceProjectiveOpen.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FormalExistenceProjectiveOpen.lean#L22). The input that we call the limit fact is named `twisted_sections_finite_generators`, but its set $W_n$ carries no finiteness condition. The hypothesis that each $S_e$ is killed by $J = 0$ is discarded with `_` in the proof of the second theorem. The name `formal_existence_projective_open` is a wrapper that closes with `first | exact ...` on the second theorem.
