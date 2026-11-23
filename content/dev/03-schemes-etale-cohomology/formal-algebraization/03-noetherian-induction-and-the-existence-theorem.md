---
title: Noetherian induction and the existence theorem for closed subschemes
decls:
  - GlobalTheory.CompanionTheory.GE.step_integral
  - GlobalTheory.CompanionTheory.GE.statement_bot
  - GlobalTheory.CompanionTheory.GE.geClosed
  - GlobalTheory.T.grothendieck_existence_closed
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Noetherian induction and the existence theorem for closed subschemes

This section completes the proof of Grothendieck's existence theorem. First we combine the proper pushforward step of Section 2 with Chow's lemma and the Artin and Rees lemma. This gives the inductive step for an ideal sheaf $J$ with $V(J)$ integral. A Noetherian induction on $J$ then proves $\mathrm{St}(0)$ on each separated scheme of finite type over $A$. Last, we apply this to the structure sheaf and get the existence theorem for closed subschemes: a compatible system of closed subschemes of the thickenings of $X$ with proper reduction comes from one closed subscheme of $X$, proper over $A$. This is EGA III_1, Théorème 5.1.4, in the form for closed subschemes. The form for closed subschemes is used in the algebraization of formal morphisms.

We keep the notation of Sections 1 and 2. For a submodule $D \subseteq E$, a closed system $(S_e)$ in $E$ and $c \geq 0$, the *restricted system* is the sequence of submodules of $D$
$$S^D_e = (S_{e+c} \cap D) + I^{e+1} D, \qquad e \geq 0.$$

**Theorem 7.3.1 (The integral step).** Let $A$ be Noetherian and $I$-adically complete, and let $X$ be separated, locally of finite type and quasi-compact over $\operatorname{Spec} A$. Let $J \subseteq \mathcal{O}_X$ be a quasi-coherent ideal sheaf with $V(J)$ integral. Assume that $\mathrm{St}(J')$ holds on $X$ for each quasi-coherent ideal sheaf $J' \supsetneq J$. Then $\mathrm{St}(J)$ holds on $X$.

Lean: `GlobalTheory.CompanionTheory.GE.step_integral`.

*Proof.* The scheme $V(J)$ is separated, locally of finite type and quasi-compact over $A$, since $V(J) \to X$ is a closed immersion. We take the following inputs as given.

1. *Chow's lemma for an integral scheme.* There are $N \geq 0$, a closed immersion $i : Y \to \mathbb{P}^N_A$, an open subscheme $O \subseteq Y$, a proper morphism $\psi : O \to V(J)$ over $A$ and a nonempty open $W \subseteq V(J)$ such that $\psi^{-1}(W) \to W$ is an isomorphism (EGA II, Théorème 5.6.1).
2. *Artin and Rees for closed systems.* Let $E$ be coherent, $(S_e)$ a closed system in $E$ with $S_0$ of proper support, $D \subseteq E$ quasi-coherent and $c \geq 0$ with $S_{e+c} \subseteq D + I^{e+1} E$ for each $e$. Then there is $c' \geq 0$ such that the restricted system $(S^D_e)$ with shift $c'$ is a closed system in $D$, its term of index $0$ has proper support, and the following holds: if the restricted system is algebraizable and $D$ has proper support, then $(S_e)$ is algebraizable.
3. A quasi-coherent submodule of a coherent module on a locally Noetherian scheme is coherent.
4. If $J'$ kills $D$ modulo each $S_n$, in the sense of the fourth claim of [Theorem 7.2.1](/entry/core-integral-step/), then each term of the restricted system is killed by $J'$, for each shift.

Let $E$ be coherent and $(S_e)$ a closed system in $E$ such that each $S_e$ is killed by $J$ and $S_0$ has proper support. Take $N$, $Y$, $i$, $O$, $\psi$ and $W$ from Chow's lemma. View $O$ over $A$ through $O \to Y \to \mathbb{P}^N_A \to \operatorname{Spec} A$. By [Theorem 7.1.5](/entry/statement-open-projective/), $\mathrm{St}(0)$ holds on $O$. The map $\iota \circ \psi : O \to X$ is a morphism over $A$, by the compatibility in Chow's lemma. So [Theorem 7.2.1](/entry/core-integral-step/) applies. It gives $D$, $c$ and $J'$ with $D$ quasi-coherent and of proper support, $S_{e+c} \subseteq D + I^{e+1} E$, $J \subsetneq J'$, and $J'$ kills $D$ modulo each $S_n$.

The Artin and Rees input gives $c'$. The restricted system with shift $c'$ is a closed system in $D$, and its term of index $0$ has proper support. The module $D$ is coherent by the third input, and each term of the restricted system is killed by $J'$ by the fourth input. So the induction hypothesis $\mathrm{St}(J')$ applies to $D$ and the restricted system, and the restricted system is algebraizable. Since $D$ has proper support, the Artin and Rees input shows that $(S_e)$ is algebraizable. $\square$

**Theorem 7.3.2 (Existence for coherent quotients).** Let $A$ be Noetherian and $I$-adically complete, and let $X$ be separated, locally of finite type and quasi-compact over $\operatorname{Spec} A$. Then $\mathrm{St}(0)$ holds on $X$. That is, for each coherent $\mathcal{O}_X$-module $E$ and each closed system $(S_e)$ in $E$ such that $S_0$ has proper support, there is a quasi-coherent $B \subseteq E$ with proper support and $B + I^{e+1} E = S_e$ for each $e \geq 0$.

Lean: `GlobalTheory.CompanionTheory.GE.statement_bot`.

*Proof.* The scheme $X$ is locally Noetherian and quasi-compact, so it is Noetherian. We take as given four inputs.

1. On a Noetherian scheme each strictly increasing sequence of quasi-coherent ideal sheaves is finite. So we may use induction on $J$ for the order $\supsetneq$.
2. $\mathrm{St}(\mathcal{O}_X)$ holds: for $J = \mathcal{O}_X$ each $S_e$ is all of $E$, and $B = E$ works.
3. Let $J \neq \mathcal{O}_X$. Then either $V(J)$ is integral, or there are quasi-coherent ideal sheaves $J_1, J_2 \supsetneq J$ such that $a b \in J(U)$ for each affine open $U$, each $a \in J_1(U)$ and each $b \in J_2(U)$.
4. In the second case of the third input, $\mathrm{St}(J_1)$ and $\mathrm{St}(J_2)$ imply $\mathrm{St}(J)$.

We prove $\mathrm{St}(J)$ for each $J$ by induction for the order $\supsetneq$, and then take $J = 0$. Let $J$ be given and assume $\mathrm{St}(J')$ for each $J' \supsetneq J$. If $J = \mathcal{O}_X$, the second input applies. Otherwise we use the third input. If $V(J)$ is integral, the integral step above gives $\mathrm{St}(J)$. In the other case the induction hypothesis gives $\mathrm{St}(J_1)$ and $\mathrm{St}(J_2)$, and the fourth input gives $\mathrm{St}(J)$. $\square$

Now we turn to closed subschemes. Let $R$ be a ring, $I \subseteq R$ an ideal and $P$ a scheme over $\operatorname{Spec} R$. For $e \geq 0$ let $P_e = P \times_R \operatorname{Spec} R/I^{e+1}$, with the closed immersions $P_e \to P_{e+1}$ and $P_e \to P$.

**Theorem 7.3.3 (Grothendieck's existence theorem for closed subschemes).** Let $R$ be Noetherian and $I$-adically complete. Let $P$ be separated, locally of finite type and quasi-compact over $\operatorname{Spec} R$. Let $(C_e)_{e \geq 0}$ be schemes with closed immersions $i_e : C_e \to P_e$ and morphisms $\beta_e : C_e \to C_{e+1}$ such that, for each $e$, the square formed by $\beta_e$, $i_e$, $i_{e+1}$ and $P_e \to P_{e+1}$ is a pullback square. Assume that $C_0 \to \operatorname{Spec} R/I$ is proper. Then there are a scheme $C'$, a closed immersion $j : C' \to P$ and morphisms $b_e : C_e \to C'$ with these properties.

1. $C'$ is proper over $\operatorname{Spec} R$.
2. For each $e$, the square formed by $b_e$, $i_e$, $j$ and $P_e \to P$ is a pullback square, so $C_e = C' \times_P P_e$.
3. $b_{e+1} \circ \beta_e = b_e$ for each $e$.

Lean: `GlobalTheory.CompanionTheory.GE.geClosed` (also `GlobalTheory.T.grothendieck_existence_closed`, a second name).

*Proof.* We apply the existence for coherent quotients to $E = \mathcal{O}_P$. Let $c_e : C_e \to P$ be the composite of $i_e$ and $P_e \to P$. It is a closed immersion. Let $J_e \subseteq \mathcal{O}_P$ be its ideal sheaf, and let $Q_e$ be the ideal sheaf of $P_e$ in $P$, so $Q_e = I^{e+1} \mathcal{O}_P$. Then $Q_e \subseteq J_e$, since $c_e$ factors through $P_e$. The pullback square for $\beta_e$ gives $J_e = J_{e+1} + Q_e$. So $(J_e)$ is a closed system in $\mathcal{O}_P$. The quotient $\mathcal{O}_P / J_0$ is the structure sheaf of $C_0$, and $C_0$ is proper over $R/I$ and so over $R$. Since $P$ is separated, the support of $\mathcal{O}_P / J_0$ is a proper closed subscheme, and $J_0$ has proper support.

The existence for coherent quotients gives a quasi-coherent $B \subseteq \mathcal{O}_P$ with proper support and $B + I^{e+1} \mathcal{O}_P = J_e$ for each $e$. A quasi-coherent submodule of $\mathcal{O}_P$ is an ideal sheaf. Let $C' = V(B)$ and let $j : C' \to P$ be the closed immersion. Then $C'$ is proper over $R$, by the support condition and the separatedness of $P$. Since $B \subseteq J_e$, the map $c_e$ factors through $j$ in a unique way, as $c_e = j \circ b_e$. The equality $B + Q_e = J_e$ says that $C_e$ is the scheme theoretic intersection of $C'$ and $P_e$, which is the pullback claim. The compatibility $b_{e+1} \circ \beta_e = b_e$ holds because both sides composed with the monomorphism $j$ give $c_e$. $\square$

The theorem is the first input of the algebraization of formal morphisms, which is part of the theorem of Section 6. In the standard argument $P$ is the product $X \times_R Z$ of the two schemes and $C_e$ is the graph of the given morphism on the $e$-th thickening. A second input then shows that the projection from $C'$ to $X$ is an isomorphism.

**Remark 7.3.4 (Formalization).** The three theorems are in [GrothendieckExistenceClosed.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GrothendieckExistenceClosed.lean#L22). The induction uses the well-founded order on ideal sheaves, with motive $\mathrm{St}(J)$. The proof of the last theorem is one line: it is `T.geClosed_of_statement_bot` applied to the second theorem. That wrapper is in [GrothendieckExistenceClosedAltBis.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GrothendieckExistenceClosedAltBis.lean#L6) and closes with `first | exact ...` on `Close.geClosed_of_statement`, whose proof is in [GeClosedOfStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GeClosedOfStatement.lean#L356). The definition `GEClosed` is in [GEClosedProj.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FormalAlgebraisation/GEClosedProj.lean#L13).
