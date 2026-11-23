---
title: Gauss norms and proportional eigenvectors in A_cris
decls:
  - GlobalTheory.PMon.Gauss.ratio_proportional_target
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gauss norms and proportional eigenvectors in A_cris

This section proves the statement in $A_{\mathrm{cris}}$ behind [the ratio of integral eigenvectors](/entry/ratio-integral/) of section 16. Let $w, w'$ be eigenvectors of $\varphi^h$ in $A_{\mathrm{cris}}$ with eigenvalue $\ell^s$, $s < h$, and assume that $\varphi(w)\, w' = w\, \varphi(w')$. Then $w$ and $w'$ are proportional over $\mathbb{Z}_\ell$: there are $c, d \in \mathbb{Z}_\ell$ with $c \neq 0$ and $c\, w = d\, w'$. The relation says that the ratio $w / w'$ is fixed by $\varphi$, and the $\varphi$-fixed elements of $A_{\mathrm{cris}}$ are the elements of $\mathbb{Z}_\ell$. Since $A_{\mathrm{cris}}$ is not a field, we cannot divide. Instead we compare $w$ and $w'$ with a family of norms, one for each radius, and we find the digits of the ratio one at a time.

We keep the notation of section 16: Fontaine's rings $A_{\inf} = W(\mathcal{O}_C^\flat)$ and $A_{\mathrm{cris}}$, the map $A_{\inf} \to A_{\mathrm{cris}}$, and the Frobenius $\varphi$ of $A_{\mathrm{cris}}$ (see [[Fontaine's period rings|K6HW8YWCQJ]] and [crystalline representations](/learn/padic-hodge/#crystalline-and-semistable-representations)). We view $\mathbb{Z}_\ell$ as a subring of $A_{\mathrm{cris}}$ through $A_{\inf}$. For $x \in \mathcal{O}_C^\flat$ let $x^\sharp \in \mathcal{O}_{\mathbb{C}_\ell}$ be its untilt.

**Definition 6.22.1 (Gauss norms).** Let $\ell^{-1} \leq \rho < 1$. For $a \in A_{\inf}$ with Witt coordinates $(a_0, a_1, \dots)$ in $\mathcal{O}_C^\flat$, put
$$|a|_\rho = \sup_{n \geq 0} \, |a_n^\sharp|^{1/\ell^n} \rho^n.$$
A *Gauss norm of radius $\rho$* on $A_{\mathrm{cris}}$ is a map $N : A_{\mathrm{cris}} \to \mathbb{R}$ with $0 \leq N(x) \leq 1$, $N(x + y) \leq \max(N(x), N(y))$, $N(-x) = N(x)$ and $N(xy) = N(x) N(y)$ for all $x, y$, and $N(a) = |a|_\rho$ for every $a \in A_{\inf}$. When a Gauss norm of radius $\rho$ exists we fix one and call it $N_\rho$. For $0 < r \leq 1$ put $v_r(x) = -\log_\ell N_{\ell^{-r}}(x)$.

Lean: `GlobalTheory.PMon.Gauss.IsGauss` (also `GlobalTheory.PMon.Gauss.gC`, the chosen norm, and `GlobalTheory.PMon.Gauss.vr`, the valuation).

Since $a = \sum_n [a_n^{1/\ell^n}]\, \ell^n$, the number $|a|_\rho$ is the usual Gauss norm of the expansion of $a$ in powers of $\ell$ with Teichmüller coefficients. The radius $\rho$ plays the part of $|\ell|$, so the norms with different $\rho$ weigh the powers of $\ell$ against the size of the coefficients in different ways. A single norm cannot see whether $w$ and $w'$ are proportional; the whole family can.

We use the following facts, proved elsewhere in this development. Let $\ell^{-1} \leq \rho < 1$.

1. $N_\rho$ exists and is a Gauss norm of radius $\rho$. We have $N_\rho(1) = 1$ and $N_\rho(\ell) = \rho$, so $N_\rho(\ell^m x) = \rho^m N_\rho(x)$ for $m \geq 0$.
2. $N_\rho(x) > 0$ for every $x \neq 0$.
3. $\varphi(c) = c$ for $c \in \mathbb{Z}_\ell$.
4. (Slopes.) Let $s < h$ and $w, w' \in A_{\mathrm{cris}}$ with $\varphi^h(w') = \ell^s w'$, $w \neq 0$, $w' \neq 0$ and $\varphi(w)\, w' = w\, \varphi(w')$. Then there is $n \in \mathbb{Z}$ with $v_r(w) - v_r(w') = n r$ for all $r \in (0, 1]$.
5. (Leading digit.) Let $s < h$ and $w, w' \in A_{\mathrm{cris}}$ with $\varphi^h(w') = \ell^s w'$, $w' \neq 0$, $\varphi(w)\, w' = w\, \varphi(w')$ and $N_\rho(w) = N_\rho(w')$ for all $\rho \in [\ell^{-1}, 1)$. Then there is a unit $c \in \mathbb{Z}_\ell^\times$ with $N_\rho(w - c w') \leq \rho\, N_\rho(w')$ for all $\rho \in [\ell^{-1}, 1)$.

Fact 4 says that $w$ and $w'$ have the same Newton polygon up to a shift by an integer $n$. In terms of norms: $N_\rho(w) = \rho^n N_\rho(w')$ for all $\rho \in [\ell^{-1}, 1)$. Indeed, put $r = -\log_\ell \rho \in (0, 1]$; then $\log_\ell N_\rho(w) = \log_\ell N_\rho(w') - n r = \log_\ell(\rho^n N_\rho(w'))$, and both sides are logarithms of positive numbers by fact 2. Fact 5 is the first digit of the ratio $w / w'$, read off modulo $\ell$.

**Lemma 6.22.2 (Equal norms give a constant ratio).** Let $s < h$ and $W, W' \in A_{\mathrm{cris}}$ with $\varphi^h(W') = \ell^s W'$, $W' \neq 0$, $\varphi(W)\, W' = W\, \varphi(W')$, and $N_\rho(W) = N_\rho(W')$ for all $\rho \in [\ell^{-1}, 1)$. Then $W = c\, W'$ for some $c \in \mathbb{Z}_\ell$.

Lean: `GlobalTheory.PMon.Gauss.RatioProp.eq_zc_mul` (also `GlobalTheory.PMon.Gauss.RatioProp.digit_step`, the inductive step).

*Proof.* For $k \geq 0$ let $D_k$ be the set of $c \in \mathbb{Z}_\ell$ with
$$N_\rho(W - c\, W') \leq \rho^k N_\rho(W') \quad \text{for all } \rho \in [\ell^{-1}, 1).$$
Then $0 \in D_0$, since $N_\rho(W) = N_\rho(W')$, and $D_{k+1} \subseteq D_k$, since $\rho^{k+1} \leq \rho^k$.

Each $D_k$ is closed. Let $c' \in \mathbb{Z}_\ell$ with $c - c' \in \ell^k \mathbb{Z}_\ell$, say $c = c' + \ell^k y$. Then $W - c W' = (W - c' W') - \ell^k y W'$, and $N_\rho(\ell^k y W') = \rho^k N_\rho(y) N_\rho(W') \leq \rho^k N_\rho(W')$. By the ultrametric inequality, $c \in D_k$ if and only if $c' \in D_k$. So $D_k$ is a union of cosets of $\ell^k \mathbb{Z}_\ell$, hence closed.

Each $D_k$ is nonempty. We use induction on $k$. Let $c \in D_k$ and put $V = W - c\, W'$. Since $\varphi(c) = c$ by fact 3, $V$ satisfies $\varphi(V)\, W' = V\, \varphi(W')$. If $V = 0$, then $c \in D_{k+1}$. If $V \neq 0$, fact 4 gives $n \in \mathbb{Z}$ with $N_\rho(V) = \rho^n N_\rho(W')$ for all $\rho$. At $\rho = \ell^{-1}$ the condition $c \in D_k$ gives $\ell^{-n} \leq \ell^{-k}$, so $n \geq k$. The elements $V$ and $\ell^n W'$ have the same norms, $\ell^n W'$ is an eigenvector of $\varphi^h$ with eigenvalue $\ell^s$, and $\varphi(V)\, \ell^n W' = V\, \varphi(\ell^n W')$. Fact 5 gives a unit $u$ with
$$N_\rho(V - u \ell^n W') \leq \rho\, N_\rho(\ell^n W') = \rho^{n+1} N_\rho(W') \leq \rho^{k+1} N_\rho(W').$$
Since $V - u \ell^n W' = W - (c + u \ell^n) W'$, we get $c + u \ell^n \in D_{k+1}$.

The sets $D_k$ are a decreasing sequence of nonempty closed subsets of the compact space $\mathbb{Z}_\ell$. So their intersection contains some $c$. Then $N_{1/\ell}(W - c W') \leq \ell^{-k} N_{1/\ell}(W')$ for every $k$, so $N_{1/\ell}(W - c W') = 0$, and $W = c\, W'$ by fact 2. $\square$

**Theorem 6.22.3 (Proportional eigenvectors).** Let $\ell$ be a prime, $s < h$, and $w, w' \in A_{\mathrm{cris}}$ with
$$\varphi^h(w) = \ell^s w, \qquad \varphi^h(w') = \ell^s w', \qquad w' \neq 0, \qquad \varphi(w)\, w' = w\, \varphi(w').$$
Then there are $c, d \in \mathbb{Z}_\ell$ with $c \neq 0$ and $c\, w = d\, w'$.

Lean: `GlobalTheory.PMon.Gauss.ratio_proportional_target`.

*Proof.* If $w = 0$, take $c = 1$ and $d = 0$. Let $w \neq 0$. By fact 4 there is $n \in \mathbb{Z}$ with $N_\rho(w) = \rho^n N_\rho(w')$ for all $\rho \in [\ell^{-1}, 1)$.

Let $n = m \geq 0$. Put $W = w$ and $W' = \ell^m w'$. Then $W' \neq 0$, since $N_\rho(W') = \rho^m N_\rho(w') > 0$, and $\varphi^h(W') = \ell^s W'$. The relation for $(w, w')$ multiplied by $\ell^m$ is the relation for $(W, W')$, because $\varphi(\ell) = \ell$. By fact 1, $N_\rho(W') = \rho^m N_\rho(w') = N_\rho(W)$. The Lemma gives $c$ with $w = c\, \ell^m w'$. So $1 \cdot w = (c \ell^m)\, w'$.

Let $n = -m < 0$. Put $W = \ell^m w$ and $W' = w'$. In the same way $N_\rho(W) = \rho^m \rho^{-m} N_\rho(w') = N_\rho(W')$, and the relation holds for $(W, W')$. The Lemma gives $c$ with $\ell^m w = c\, w'$, and $\ell^m \neq 0$ in $\mathbb{Z}_\ell$. $\square$

Through the tie of the period data, [the ratio of integral eigenvectors](/entry/ratio-integral/) transports this result from $A_{\mathrm{cris}}$ to $B$, and from there it reaches the Moore determinant of section 16 and the lattice lemma of section 20.

**Remark 6.22.4 (Formalization).** The hypothesis $\varphi^h(w) = \ell^s w$ is introduced as `_` and not used ([RatioProportionalTarget.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RatioProportionalTarget.lean#L194)); only $w'$ needs to be an eigenvector. The norm $N_\rho$ is `gC`, defined with `Classical.choose` among all Gauss norms of radius $\rho$, and with value $0$ when there is none; facts 1 and 2 are `isGauss_gC_target`, `GlobalTheory.T.gaussNormAcris_basic_values` and `GlobalTheory.T.gaussNormAcrisRadius_pos_definite`. Facts 4 and 5 are `GlobalTheory.T.acrisValuation_sub_eq_int_mul_radius` and `GlobalTheory.T.gaussNormAcris_sub_unit_le_digit`; we read their statements, not their proofs. The sets $D_k$ are `digitSet`, and the compactness step is `IsCompact.nonempty_iInter_of_sequence_nonempty_isCompact_isClosed`.
