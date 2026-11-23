---
title: The proper pushforward step
decls:
  - GlobalTheory.CompanionTheory.GE.core_integral_step
  - GlobalTheory.T.formal_existence_proper_pushforward
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The proper pushforward step

This section proves the step of the induction in which the closed subscheme $V(J)$ is integral. We are given a proper map $\psi : Z \to V(J)$ that is an isomorphism over a nonempty open subset, and we know the existence statement on $Z$. From these we build a quasi-coherent submodule $D$ of $E$ that algebraizes the system up to a shift, and an ideal sheaf $J'$ strictly larger than $J$ that kills $D$ modulo the system. Section 3 combines this with the Artin and Rees lemma and the induction hypothesis at $J'$. The construction is the pushforward argument of EGA III_1, §5.1, through Chow's lemma.

We keep the notation of Section 1: $A$ is Noetherian, $I \subseteq A$ an ideal, and for a scheme $X$ over $\operatorname{Spec} A$ we have closed systems, proper support, the killing condition and the statement $\mathrm{St}(J)$. For a morphism $\varphi : Z \to X$ over $A$, a quasi-coherent module $E$ on $X$ and a submodule $B \subseteq \varphi^* E$, let
$$D_\varphi(B) = \ker\big(E \to \varphi_* \varphi^* E \to \varphi_*(\varphi^* E / B)\big),$$
where the first map is the unit of the adjunction. This is the largest submodule of $E$ whose pullback maps into $B$.

**Theorem 7.2.1 (Proper pushforward step).** Let $A$ be Noetherian and $I$-adically complete. Let $X$ be separated, locally of finite type and quasi-compact over $\operatorname{Spec} A$. Let $J \subseteq \mathcal{O}_X$ be a quasi-coherent ideal sheaf with $V(J)$ integral, with closed immersion $\iota : V(J) \to X$. Let $Z$ be a scheme over $\operatorname{Spec} A$ such that $\mathrm{St}(0)$ holds on $Z$. Let $\psi : Z \to V(J)$ be proper with $\iota \circ \psi$ a morphism over $A$, and let $W \subseteq V(J)$ be a nonempty open subset such that the restriction $\psi^{-1}(W) \to W$ is an isomorphism. Let $E$ be a coherent $\mathcal{O}_X$-module and $(S_e)$ a closed system in $E$ such that each $S_e$ is killed by $J$ and $S_0$ has proper support. Then there are a submodule $D \subseteq E$, an integer $c \geq 0$ and a quasi-coherent ideal sheaf $J' \subseteq \mathcal{O}_X$ with the following properties.

1. $D$ is quasi-coherent and has proper support.
2. $S_{e+c} \subseteq D + I^{e+1} E$ for each $e \geq 0$.
3. $J \subsetneq J'$.
4. For each $n \geq 0$, each affine open $U$, each $a \in J'(U)$ and each $x$ in the image of $D(U) \to E(U)$, we have $a x \in S_n(U)$.

Lean: `GlobalTheory.CompanionTheory.GE.core_integral_step` (also `GlobalTheory.T.formal_existence_proper_pushforward`, a second name).

So $D$ algebraizes the system up to the shift $c$, and modulo the system $D$ is a module on the smaller closed subscheme $V(J')$. The theorem does not say that $D \subseteq S_n$; in general it is not.

*Proof.* As in Section 1, $X$ is locally Noetherian and quasi-compact. Let $\varphi = \iota \circ \psi : Z \to X$. It is proper, since $\psi$ is proper and $\iota$ is a closed immersion. We take as given the inputs below, which are standard facts on the pullback and pushforward of coherent modules along a proper map (EGA III_1, §3 and §5.1).

1. The system $(\varphi^* S_e)$, more precisely the system of images of $\varphi^* S_e \to \varphi^* E$, is a closed system in $\varphi^* E$.
2. Its term of index $0$ has proper support, because $S_0$ has proper support and $\varphi$ is proper.
3. If $G$ is coherent on $Z$, then $\varphi_* G$ is coherent on $X$.
4. If $B \subseteq \varphi^* E$ is quasi-coherent and algebraizes the pulled back system, then there is $c \geq 0$ with $S_{e+c} \subseteq D_\varphi(B) + I^{e+1} E$ for each $e$. This is the Artin and Rees argument for the pushforward.
5. If $B$ has proper support on $Z$, then $D_\varphi(B)$ has proper support on $X$.
6. There is a quasi-coherent ideal sheaf $J_0 \subseteq \mathcal{O}_X$ such that, for each affine open $V$ and each $f \in J_0(V)$, the inverse image in $V(J)$ of the open set $X_f$ where $f$ does not vanish is contained in $W$. Since $W$ is nonempty, $J_0^m \not\subseteq J$ for each $m \geq 0$.
7. Let $D \subseteq E$ be quasi-coherent and $(S_n)$ quasi-coherent. If for each affine open $V$, each $f \in J_0(V)$ and each $x \in D(V)$ there is $k$ with $f^k x \in S_n(V)$ for all $n$, then there is $m$ with $J_0^m D \subseteq S_n$ for all $n$. This is a Noetherian finiteness statement.
8. In the situation of the theorem, with $B$ as in the fourth input, the hypothesis of the seventh input holds for $D = D_\varphi(B)$. The reason is that over $X_f$ the map $\psi$ is an isomorphism, so $D_\varphi(B)$ and $S_n$ agree there, because each $S_n$ is killed by $J$.

Now the first and second inputs show that the pulled back system satisfies the hypotheses of $\mathrm{St}(0)$ on $Z$. Here $\varphi^* E$ is coherent, and the killing condition for the zero ideal holds, since $0 \cdot x = 0$. So $\mathrm{St}(0)$ gives a quasi-coherent $B \subseteq \varphi^* E$ with proper support that algebraizes the pulled back system. The cokernel $\varphi^* E / B$ is coherent, so by the third input its pushforward is coherent. Let $D = D_\varphi(B)$. It is the kernel of a map of coherent modules, so it is quasi-coherent. The fifth input gives that $D$ has proper support, and the fourth input gives $c$. This proves the first two claims.

Take $J_0$ from the sixth input. The seventh and eighth inputs give $m$ with $a x \in S_n(U)$ for each $n$, each affine open $U$, each $a \in J_0^m(U)$ and each $x$ in the image of $D(U)$. Let $J' = J + J_0^m$. Then $J \subseteq J'$, and $J' \neq J$ because $J_0^m \not\subseteq J$. This is the third claim.

For the fourth claim, let $a \in J'(U)$ and let $x$ be in the image of $D(U)$. Write $a = a_1 + a_2$ with $a_1 \in J(U)$ and $a_2 \in J_0^m(U)$. Since $S_n$ is killed by $J$, we have $a_1 x \in S_n(U)$. By the choice of $m$, we have $a_2 x \in S_n(U)$. So $a x = a_1 x + a_2 x \in S_n(U)$. $\square$

The theorem uses $\mathrm{St}(0)$ on $Z$ only for the pulled back system. In Section 3 the scheme $Z$ is an open subscheme of a projective scheme, and $\mathrm{St}(0)$ on $Z$ is given by [Theorem 7.1.5](/entry/statement-open-projective/) on open subschemes of projective schemes. In Section 3 the integrality of $V(J)$ is what gives $\psi$, by Chow's lemma.

**Remark 7.2.2 (Formalization).** The theorem is in [FormalExistenceProperPushforward.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FormalExistenceProperPushforward.lean#L21). The submodule $D_\varphi(B)$ is `adjKer φ B`. The fifth input is `T.pushforward_closed_system_auxiliary`, which is stated in the file `PushforwardClosedSystemUnseenStatement.lean`, so the name of the file and the name of the theorem do not match. The sixth input, `T.nonempty_open_ideal_not_nilpotent`, has no integrality hypothesis. The killing condition for the zero ideal on $Z$ is proved inline from $a = 0$. The name `formal_existence_proper_pushforward` is a wrapper that closes with `first | exact ...`.
