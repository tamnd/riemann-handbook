---
title: The Leibniz rule with ordered layers
decls:
  - GlobalTheory.T.leibniz_order_of_exact_sequences
  - GlobalTheory.CompanionTheory.LeibOrd.Main.leibnizOrd_of_parts
  - GlobalTheory.CompanionTheory.LeibOrd.Main.main_chain
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Leibniz rule with ordered layers

The derivative of a product of two representations of general linear groups is built from products of derivatives of the factors. This section proves that rule, with the layers in a fixed order, from six facts about $\Phi$ and $\Psi$ on mirabolic products; three of them are the subject of the earlier sections. The Leibniz rule [Theorem 7.5.2](/entry/leibniz-ord/) passes the six facts to the theorem proved here, on the way to the unitary dual of $\mathrm{GL}_n$ and the step [EveryCharacter](/step/every-character/). The argument is an induction that splits off one layer for each application of $\Phi$.

### Derivatives

We keep the notation of the earlier sections: $k$ is a nonarchimedean local field, $\psi$ a continuous nontrivial character of $k$, $G_N = \mathrm{GL}_N(k)$, $P_N$ its mirabolic subgroup and $\nu = |\det|$. For $\tau$ on $P_N$, the normalized functors give $\Phi\tau$ on $P_{N-1}$ (for $N \geq 2$) and $\Psi\tau$ on $G_{N-1}$. For $\rho$ on $G_m$, $\tau$ on $P_l$ and $\sigma$ on $G_t$, the products $\rho \times \tau$ and $\tau \times \sigma$ live on $P_{m+l}$ and $P_{l+t}$. For $\pi_1$ on $G_r$ and $\pi_2$ on $G_t$, $\pi_1 \times \pi_2$ is normalized parabolic induction to $G_{r+t}$, and $\pi|_P$ is restriction to the mirabolic subgroup.

**Definition 1.9.1 (Derivatives).** Let $\tau$ be a representation of $P_{N+1}$ and $0 \leq j \leq N$. Put $\tau^{[j]} = \Psi\Phi^{j}\tau$, a representation of $G_{N-j}$. For $\pi$ on $G_N$ put $d_0\pi = \pi$ and $d_j\pi = (\pi|_P)^{[j-1]}$ for $1 \leq j \leq N$, a representation of $G_{N-j}$. The $j$-th derivative $\pi^{(j)}$ is defined in the same way with the unnormalized functors $\Phi^-$ and $\Psi^-$.

Note that $\tau^{[j+1]} = (\Phi\tau)^{[j]}$; this lets an induction on $j$ pass from $\tau$ to $\Phi\tau$.

### The statement

**Theorem 1.9.2 (Bernstein and Zelevinsky).** Let $\rho$ and $\pi$ be smooth representations of $G_r$ and $G_t$, and let $\ell \geq 0$. Then $(\rho \times \pi)^{(\ell)}$ is glued from the representations $\rho^{(i)} \times \pi^{(\ell - i)}$, $0 \leq i \leq \ell$, where terms with $i > r$ or $\ell - i > t$ are omitted.

This is the Leibniz rule of Bernstein and Zelevinsky (Ann. Sci. ENS (4) 10 (1977), Section 4). With their normalization no twists appear. The form proved here records the order of the layers and the twists of our normalization.

The six facts are the following; the representations are smooth, and in (F3), (F5), (F6) $\psi$ is continuous and nontrivial.

- (F1) For $\pi_1$ on $G_{r}$ and $\pi_2$ on $G_{t}$ with $r, t \geq 1$, $(\pi_1 \times \pi_2)|_P$ has a subrepresentation isomorphic to $(\pi_1|_P) \times \pi_2$ with quotient isomorphic to $\pi_1 \times (\pi_2|_P)$.
- (F2) $\Psi(\rho \times \tau) \cong \rho \times \Psi\tau$.
- (F3) $\Phi(\rho \times \tau) \cong \rho \times \Phi\tau$ for $\tau$ on $P_l$, $l \geq 2$; see [Theorem 1.5.12](/entry/phi-gp/).
- (F4) $\Psi(\tau \times \sigma) \cong \Psi\tau \times \sigma$.
- (F5) For $\tau$ on $P_l$ and $\sigma$ on $G_s$ with $l \geq 2$ and $s \geq 1$, $\Phi(\tau \times \sigma)$ has a subrepresentation isomorphic to $\Phi\tau \times \sigma$ with quotient isomorphic to $\Psi\tau \times \sigma|_P$; see [Theorem 1.8.2](/entry/phi-pg/).
- (F6) For $\tau$ on $P_1$ and $\sigma$ on $G_s$, $s \geq 1$, $\Phi(\tau \times \sigma) \cong \Psi\tau \times \sigma|_P$; see [Theorem 1.6.2](/entry/phi-pg0-holds/).

**Theorem 1.9.3 (The Leibniz rule with ordered layers).** Assume (F1) to (F6). Let $r, t, \ell, n \geq 0$ with $r + t = n + \ell$, and let $\pi_1$, $\pi_2$ be smooth representations of $G_r$ and $G_t$. Then $D = (\pi_1 \times \pi_2)^{(\ell)}$ has subrepresentations $D = F_0 \supseteq F_1 \supseteq \dots \supseteq F_{\ell+1} = 0$ such that for $0 \leq i \leq \ell$:

- if $i \leq r$ and $\ell - i \leq t$, then $F_i / F_{i+1} \cong \pi_1^{(i)}\nu^{(\ell-i)/2} \times \pi_2^{(\ell-i)}\nu^{i/2}$;
- otherwise $F_i = F_{i+1}$.

Lean: `GlobalTheory.CompanionTheory.LeibOrd.Main.leibnizOrd_of_parts` (also `GlobalTheory.T.leibniz_order_of_exact_sequences`, the same statement).

The top layer carries all derivatives on $\pi_2$; each step down moves one to $\pi_1$.

We take the following facts as given; they are proved elsewhere in the development.

**Theorem 1.9.4 (Inputs).**

- (i) $\Phi$ and $\Psi$ carry isomorphic representations to isomorphic representations, and they carry short exact sequences of smooth representations to short exact sequences; for $\Phi$ this uses the continuity of $\psi$. A zero representation goes to zero.
- (ii) For $\rho$ on $G_m$ and $\tau$ on $P_1$, $\Phi(\rho \times \tau) = 0$.
- (iii) For $\tau$ on $P_l$, $l \geq 2$, and $\sigma$ on $G_0$, $\Phi(\tau \times \sigma) \cong \Phi\tau \times \sigma$.
- (iv) Let $\pi_1$ be on $G_r$ and $\pi_2$ on $G_t$. If $r = 0$ and $t \geq 1$, then $(\pi_1 \times \pi_2)|_P \cong \pi_1 \times (\pi_2|_P)$. If $t = 0$ and $r \geq 1$, then $(\pi_1 \times \pi_2)|_P \cong (\pi_1|_P) \times \pi_2$.
- (v) For $\pi$ on $G_{N}$ and $j \leq N$, $\pi^{(j)} \cong (d_j\pi)\nu^{j/2}$.
- (vi) $(A \times B)\nu^{s} \cong A\nu^{s} \times B\nu^{s}$ and $(A\nu^{s})\nu^{s'} \cong A\nu^{s+s'}$.
- (vii) Every chain (defined below) from $a$ to $b$ on $X$ gives subrepresentations $X = F_a \supseteq F_{a+1} \supseteq \dots \supseteq F_b = 0$ such that, for $a \leq c < b$, either $F_c/F_{c+1} \cong A$ for some $A$ with $R(c, A)$, or $Z(c)$ holds and $F_c = F_{c+1}$.

### Chains

The proof builds a chain, a record of how a representation is cut into pieces, and turns it into a filtration by (vii).

**Definition 1.9.5 (Chains).** Fix $n$, a relation $R(c, A)$ between indices $c$ and representations $A$ of $G_n$, and a set $Z$ of indices. A chain from $a$ to $b$ on a representation $X$ of $G_n$ is given by the following rules. If $X = 0$, there is a chain from $a$ to $a$ on $X$. If $0 \to Y \to X \to A \to 0$ is exact, $R(a, A)$ holds and there is a chain from $a + 1$ to $b$ on $Y$, there is a chain from $a$ to $b$ on $X$. If $a \in Z$, $Y \cong X$ and there is a chain from $a + 1$ to $b$ on $Y$, there is a chain from $a$ to $b$ on $X$.

A chain survives an isomorphism $X \cong X'$, a weaker $R$, a larger $Z$, and a shift of indices. Twisting by $\nu^s$ turns it into a chain for the relation "$A \cong A_0\nu^{s}$ with $R(c, A_0)$".

**Lemma 1.9.6 (Top piece).** Let $0 \to Y \to X \to C \to 0$ be exact. Suppose either $C \cong A$ with $R(a, A)$, or $a \in Z$ and $C = 0$. If $Y$ has a chain from $a + 1$ to $b$, then $X$ has a chain from $a$ to $b$.

*Proof.* In the first case compose $X \to C$ with $C \cong A$ and use the second rule. In the second, $Y \to X$ is an isomorphism and the third rule applies. $\square$

### Products of the form ρ × τ

**Lemma 1.9.7 (Derivatives of ρ × τ).** Let $\rho$ be on $G_m$ and $\tau$ on $P_{a+1}$, both smooth, and let $j \geq 0$. If $j \leq a$, then $(\rho \times \tau)^{[j]} \cong \rho \times \tau^{[j]}$. If $j > a$, then $(\rho \times \tau)^{[j]} = 0$.

*Proof.* For $j \leq a$ induct on $j$. For $j = 0$ this is (F2). For $j + 1$, (F3) gives $\Phi(\rho \times \tau) \cong \rho \times \Phi\tau$, so by (i) and induction $(\rho \times \tau)^{[j+1]} = (\Phi(\rho \times \tau))^{[j]} \cong (\rho \times \Phi\tau)^{[j]} \cong \rho \times (\Phi\tau)^{[j]} = \rho \times \tau^{[j+1]}$. For $j > a$ induct on $a$. If $a = 0$, then $j \geq 1$ and $\Phi(\rho \times \tau) = 0$ by (ii), so $(\rho \times \tau)^{[j]} = 0$ by (i). If $a \geq 1$, (F3) and (i) give $(\rho \times \tau)^{[j]} \cong (\rho \times \Phi\tau)^{[j-1]}$, which is zero by induction since $\Phi\tau$ is on $P_a$ and $j - 1 > a - 1$. $\square$

### Products of the form τ × σ

For $\tau$ on $P_{i+1}$ and $\sigma$ on $G_t$, let $R_P(a, A)$ say that $a = b + 1$ with $b + c = j$, $b \leq i$, $c \leq t$ and $A \cong \tau^{[b]} \times d_c\sigma$, and let $Z_P$ be the set of $a$ with $a > i + 1$ or $j + 1 - a > t$.

**Lemma 1.9.8 (The chain for τ × σ).** Let $\tau$ on $P_{i+1}$ and $\sigma$ on $G_t$ be smooth, with $i + t = n + j$. Then $(\tau \times \sigma)^{[j]}$ has a chain from $1$ to $j + 2$ for $R_P$ and $Z_P$.

*Proof.* Induct on $j$, for all $i$, $t$, $\tau$, $\sigma$. For $j = 0$, (F4) gives $(\tau \times \sigma)^{[0]} \cong \Psi\tau \times \sigma = \tau^{[0]} \times d_0\sigma$, which is one layer at index $1$; below it the chain on $0$ ends at $2$.

For $j + 1$ we have $(\tau \times \sigma)^{[j+1]} = (\Phi(\tau \times \sigma))^{[j]}$. The case $i = t = 0$ is impossible, since $i + t = n + j + 1$.

When $t = s + 1 \geq 1$, $Q = (\Psi\tau \times \sigma|_P)^{[j]}$ is a top piece at index $1$, with $\sigma|_P$ on $P_{s+1}$. If $j \leq s$, the lemma on $\rho \times \tau$ gives $Q \cong \Psi\tau \times (\sigma|_P)^{[j]} = \tau^{[0]} \times d_{j+1}\sigma$, which satisfies $R_P(1, Q)$ with $b = 0$ and $c = j + 1$. If $j > s$, the same lemma gives $Q = 0$, and $1 \in Z_P$ because $j + 1 > t$.

If $i = 0$ and $t \geq 1$, (F6) gives $\Phi(\tau \times \sigma) \cong \Psi\tau \times \sigma|_P$, so $(\tau \times \sigma)^{[j+1]} \cong Q$ by (i). Take $Y = 0$ in the lemma on the top piece. The zero representation has a chain from $2$ to $j + 3$, since every index $a \geq 2$ is in $Z_P$ when $i = 0$.

If $i \geq 1$ and $t = 0$, (iii) gives $\Phi(\tau \times \sigma) \cong \Phi\tau \times \sigma$. By induction, applied to $\Phi\tau$ on $P_{i}$, $(\Phi\tau \times \sigma)^{[j]}$ has a chain from $1$ to $j + 2$, and we shift it by one. A layer $(\Phi\tau)^{[b]} \times d_c\sigma$ at index $b + 1$ becomes the layer $\tau^{[b+1]} \times d_c\sigma$ at index $b + 2$, as $R_P$ for $j + 1$ requires. Index $1$ lies in $Z_P$ because $j + 1 > 0 = t$, so the third rule starts the chain at $1$.

If $i \geq 1$ and $t \geq 1$, (F5) gives an exact sequence $0 \to \Phi\tau \times \sigma \to \Phi(\tau \times \sigma) \to \Psi\tau \times \sigma|_P \to 0$. By (i) the functor $(\cdot)^{[j]}$ keeps it exact. The quotient is $Q$, the top piece at index $1$. The subrepresentation has the shifted chain of the previous case. The lemma on the top piece finishes the proof. $\square$

### The main chain

For $\pi_1$ on $G_r$ and $\pi_2$ on $G_t$, let $R_F(a, A)$ say that $a + c = \ell$, $a \leq r$, $c \leq t$ and $A \cong d_a\pi_1 \times d_c\pi_2$, and let $Z_F$ be the set of $a$ with $a > r$ or $\ell - a > t$.

**Theorem 1.9.9 (The main chain).** Assume (F1) to (F6). Let $\pi_1$ on $G_r$ and $\pi_2$ on $G_t$ be smooth, with $r + t = n + \ell$. Then $d_\ell(\pi_1 \times \pi_2)$ has a chain from $0$ to $\ell + 1$ for $R_F$ and $Z_F$.

Lean: `GlobalTheory.CompanionTheory.LeibOrd.Main.main_chain`.

*Proof.* If $\ell = 0$, $\pi_1 \times \pi_2$ is the single layer, at index $0$. Let $\ell = j + 1$, so that $d_\ell(\pi_1 \times \pi_2) = ((\pi_1 \times \pi_2)|_P)^{[j]}$. The case $r = t = 0$ is impossible.

A chain for $R_P$ and $Z_P$ on $(\pi_1|_P \times \pi_2)^{[j]}$, with $\tau = \pi_1|_P$ on $P_r$, is a chain for $R_F$ and $Z_F$. Indeed $\tau^{[b]} = d_{b+1}\pi_1$, so a layer at index $a = b + 1$ has the form $d_a\pi_1 \times d_c\pi_2$ with $a + c = \ell$. Also $Z_P$ for $i = r - 1$ is $Z_F$.

If $r = 0$, (iv) gives $(\pi_1 \times \pi_2)|_P \cong \pi_1 \times (\pi_2|_P)$. Here $t = n + \ell \geq \ell$, so the lemma on $\rho \times \tau$ gives $d_\ell(\pi_1 \times \pi_2) \cong \pi_1 \times d_\ell\pi_2$, the layer at index $0$. The indices $1, \dots, \ell$ are in $Z_F$ because $r = 0$.

If $t = 0$, (iv) gives $(\pi_1 \times \pi_2)|_P \cong (\pi_1|_P) \times \pi_2$, and the lemma on $\tau \times \sigma$ gives a chain from $1$ to $\ell + 1$. Index $0$ is in $Z_F$ because $\ell > t$.

If $r, t \geq 1$, (F1) gives $0 \to (\pi_1|_P) \times \pi_2 \to (\pi_1 \times \pi_2)|_P \to \pi_1 \times (\pi_2|_P) \to 0$, and (i) keeps it exact after $(\cdot)^{[j]}$. The subrepresentation has a chain from $1$ to $\ell + 1$ as in the case $t = 0$. For the quotient, $\pi_2|_P$ is on $P_t$. If $j \leq t - 1$, the lemma on $\rho \times \tau$ gives $(\pi_1 \times \pi_2|_P)^{[j]} \cong \pi_1 \times d_\ell\pi_2$, which is $R_F$ at index $0$. Otherwise it is zero, and $0 \in Z_F$ because $\ell > t$. The lemma on the top piece finishes the proof. $\square$

### Proof of the theorem

*Proof of the Leibniz rule with ordered layers.* Twist the main chain by $\nu^{\ell/2}$. By (v), $d_\ell(\pi_1 \times \pi_2)\nu^{\ell/2} \cong D$, so $D$ has a chain from $0$ to $\ell + 1$ whose layers at index $a$ are isomorphic to $(d_a\pi_1 \times d_c\pi_2)\nu^{\ell/2}$ with $a + c = \ell$, $a \leq r$, $c \leq t$. Let $F$ be the filtration given by (vii). Fix $i \leq \ell$.

If $i \leq r$ and $\ell - i \leq t$, then $i \notin Z_F$, so $F_i/F_{i+1}$ is a layer with $a = i$ and $c = \ell - i$. By (vi) and (v),
$$(d_i\pi_1 \times d_{\ell-i}\pi_2)\nu^{\ell/2} \cong d_i\pi_1\,\nu^{i/2}\nu^{(\ell-i)/2} \times d_{\ell-i}\pi_2\,\nu^{(\ell-i)/2}\nu^{i/2} \cong \pi_1^{(i)}\nu^{(\ell-i)/2} \times \pi_2^{(\ell-i)}\nu^{i/2}.$$
Otherwise a layer at index $i$ would need $i \leq r$ and $\ell - i \leq t$, so the index is in $Z_F$ and $F_i = F_{i+1}$. $\square$

**Remark 1.9.10 (Formalization).** The theorem is `leibnizOrd_of_parts` in [LeibnizOrderOfExactSequences.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LeibnizOrderOfExactSequences.lean#L318); the wrapper in [LeibnizOrderOfExactSequencesStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LeibnizOrderOfExactSequencesStatement.lean#L7) restates it under `maxHeartbeats 1000000`. `LeibnizOrd` and (F1) to (F5) (`ResSeq`, `PsiGP`, `PhiGP`, `PsiPG`, `PhiPG`) are in [LeibnizOrd.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/LeibnizOrders/LeibnizOrd.lean#L36); (F6) is `PhiPG0`, from a separate file. A representation of $P_{N+1}$ is an `MRep k N`, $\tau^{[j]}$ is `dN ψ j τ`, $d_j$ is `dG` and $\pi^{(j)}$ is `derivB`. The main chain is at L254, `gp_iso` and `gp_zero` (the lemma on $\rho \times \tau$) at L122 and L142, `top_gp` (the quotient $Q$) at L177, `pg_chain` at L188 and `step_iso` (the twist computation) at L303. The inputs are wrapped at L27 to L52; we did not open their proofs. `Chain` is an inductive predicate in [SubsingletonOfGiso.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SubsingletonOfGiso.lean#L34), with `RF`, `RP`, `ZP`, `ZF` at L39 to L49 and `chain_top` at L266; zero means a subsingleton space. Lean's $Z_P$ uses truncated subtraction, which agrees with ours for $a \geq 1$. Input (iii) is named `phi_product_left_rank_zero`, though the factor of rank zero is the right one, $\sigma$; its alias at L34 is `phi_product_trivial_right`.
