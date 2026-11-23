---
title: The product τ × σ in rank zero
decls:
  - GlobalTheory.T.phi_pg_rank_zero_holds
  - GlobalTheory.CompanionTheory.MirLevi.phiPG0_holds
  - GlobalTheory.CompanionTheory.MirLevi.phiPG_zero
  - GlobalTheory.CompanionTheory.MirLevi.aux0
  - GlobalTheory.CompanionTheory.MirLevi.comb_lem
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The product τ × σ in rank zero

This section introduces the second mirabolic product of Bernstein and Zelevinsky, $\tau \times \sigma$, with $\tau$ a representation of a mirabolic group and $\sigma$ a representation of a general linear group, and computes $\Phi(\tau \times \sigma)$ when $\tau$ lives on the trivial group $P_1$. The answer, $\Phi(\tau \times \sigma) \cong \Psi\tau \times \sigma|_P$, is one of the six inputs to the Leibniz rule, [Theorem 7.5.2](/entry/leibniz-ord/). The proof rests on one picture: restricted to the unipotent part, an element of a compactly induced space is a locally constant function of compact support on a vector space over $k$, and $\Phi^-$ integrates it against $\psi^{-1}$.

We keep the notation of the previous section: $G_n$, $P_n$, $U_n$, $\nu$, $\theta_\psi$, $\Phi^-$, $\Psi^-$, $\Phi$, $\Psi$, compact induction and the product $\rho \times \tau$. For $N \geq 1$ and $y \in k^{N-1}$ write $u(y) \in U_N$ for the identity plus the column $(y, 0)$ in the last column, so $\theta_\psi(u(y)) = \psi(y_{N-1})$ and $u(y)u(y') = u(y + y')$. Let $\mathcal{O}$ be the ring of integers of $k$.

### The product τ × σ

**Definition 1.6.1 (The product τ × σ).** Let $n \geq 1$ and $t \geq 0$. Split the coordinates of $k^{n+t}$ into three blocks: the first $n-1$, the middle $t$ and the last one. Let $H_{n,t} \subseteq P_{n+t}$ be the group of elements that map the span of the first and the last block into itself. These are the matrices
$$h = \begin{pmatrix} a & b & c \\ 0 & d & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad a \in G_{n-1},\ d \in G_t.$$
The map $h \mapsto \left(\begin{pmatrix} a & c \\ 0 & 1\end{pmatrix}, d\right)$ is a homomorphism $H_{n,t} \to P_n \times G_t$. For a representation $\tau$ of $P_n$ and $\sigma$ of $G_t$ put
$$\tau \mathbin{\times_0} \sigma = \operatorname{c-Ind}_{H_{n,t}}^{P_{n+t}}(\tau \otimes \sigma), \qquad \tau \times \sigma = \tau\nu^{t/2} \mathbin{\times_0} \sigma\nu^{-n/2},$$
with $\tau \otimes \sigma$ pulled back along the homomorphism.

To see that the map is a homomorphism, multiply two such matrices. The product has blocks $aa'$, $dd'$ and last column $ac' + c$, and $\begin{pmatrix} a & c \\ 0 & 1\end{pmatrix}\begin{pmatrix} a' & c' \\ 0 & 1\end{pmatrix}$ has the same entries. As for $\rho \times \tau$, the induction is unnormalized and the twists are written out; this is the second product of Bernstein and Zelevinsky (Ann. Sci. ENS (4) 10 (1977), Section 4).

### Rank zero

When $n = 1$ the first block is empty. Then $H_{1,m} = \{\mathrm{diag}(g, 1) : g \in G_m\}$, the copy of $G_m$ in $P_{m+1}$, and its projection to $P_1 = \{1\}$ is trivial. Also $Q_{0,m} = P_m$, because a block upper triangular matrix with an empty first block is any matrix. For $\tau$ on $P_1$, the group $U_1$ is trivial, so $\Psi^-\tau$ and $\Psi\tau$ are the space of $\tau$ with the trivial group $G_0$ acting.

**Theorem 1.6.2 (Φ of τ × σ in rank zero).** Let $\psi$ be a continuous character of $k$, $m \geq 1$, $\tau$ a representation of $P_1$ on $V$ and $\sigma$ a smooth representation of $G_m$ on $W$. Then
$$\Phi(\tau \times \sigma) \cong \Psi\tau \times \sigma|_{P_m}.$$

Lean: `GlobalTheory.CompanionTheory.MirLevi.phiPG0_holds` (also `GlobalTheory.T.phi_pg_rank_zero_holds`, the same statement).

The proof reduces to one computation, of $\Phi^-$ on a representation induced from $G_m$. Write $\iota(g) = \mathrm{diag}(g,1)$ for $g \in G_m$. Every $p \in P_{m+1}$ is $\iota(g)u(v)$ for exactly one $g \in G_m$ and $v \in k^m$, since $\begin{pmatrix} g & w \\ 0 & 1\end{pmatrix} = \iota(g)\, u(g^{-1}w)$. For a smooth representation $\rho$ of $G_m$ on $E$ and $f \in \operatorname{c-Ind}_{G_m}^{P_{m+1}}\rho$, put $(rf)(v) = f(u(v))$. Then $f(\iota(g)u(v)) = \rho(g)(rf)(v)$, so $r$ is injective, and $(r(u(a)f))(v) = f(u(v)u(a)) = (rf)(v + a)$. For $s \in k^\times$ let $B_s = \{v \in k^m : |v_j| \leq |s| \text{ for all } j\}$, a compact open subgroup of $k^m$. The balls are nested, so any two contain a third.

Since $f$ is smooth, $u(a)f = f$ for $a$ in some ball $B_s$, and then $rf$ is $B_s$-periodic. Since $f$ has compact support modulo $G_m$, $rf$ vanishes outside some ball $B_S$. Since $\psi$ is continuous, the image under $v \mapsto \psi(v_m)$ of a small ball is a subgroup of the circle inside a small neighbourhood of $1$, hence trivial: there is a ball on which $\psi(v_m) = 1$.

We take the following facts as given; they are proved elsewhere in the development.

**Theorem 1.6.3 (Functions on the unipotent part).** Let $\rho$ be a smooth representation of $G_m$ on $E$ and $\psi$ a continuous character of $k$.
- (i) There is a linear map $T : \operatorname{c-Ind}_{G_m}^{P_{m+1}}\rho \to E$ with $T(u(a)f) = \psi(a_m)Tf$ for $a \in k^m$, with $T(\iota(p)f) = |\det p|\,\rho(p)Tf$ for $p \in P_m$, and such that for every ball $B_s$ on which $\psi(v_m) = 1$ there is $c \neq 0$ with $Tb = c\,e$ whenever $rb = e \cdot 1_{B_s}$.
- (ii) If $\varphi : k^m \to E$ is $B_s$-periodic and vanishes outside $B_S$, there is a finite set $R \subset k^m$ with $\varphi(v) = \sum_{x \in R} 1_{B_s}(v - x)\varphi(x)$ for all $v$.
- (iii) For every ball $B_s$ and $e \in E$ there is $b \in \operatorname{c-Ind}_{G_m}^{P_{m+1}}\rho$ with $rb = e \cdot 1_{B_s}$.

A map with the properties of (i) is $Tf = \int_{k^m} \psi(v_m)^{-1}(rf)(v)\,dv$ for a Haar measure $dv$. The first property is the substitution $v \mapsto v - a$. For the second, $u(v)\iota(p) = \iota(p)u(p^{-1}v)$, the substitution $v = pw$ has Jacobian $|\det p|$, and $(pw)_m = w_m$ because the last row of $p$ is $(0,\dots,0,1)$. In the third, $c$ is the volume of $B_s$.

**Theorem 1.6.4 (Φ⁻ of an induction from G_m).** Let $\psi$ be a continuous character of $k$, $m \geq 1$ and $\rho$ a smooth representation of $G_m$ on $E$. Let $\rho'(p) = |\det p|\,\rho(p)$ for $p \in P_m$. Then $\Phi^-(\operatorname{c-Ind}_{G_m}^{P_{m+1}}\rho) \cong \rho'$.

*Proof.* Let $T$ be as in (i) and $K$ the span of the $u f - \theta_\psi(u)f$ with $u \in U_{m+1}$; then $\Phi^-$ of the induced representation is the quotient by $K$. The first property of $T$ gives $K \subseteq \ker T$.

Conversely, let $Tf = 0$. Choose a ball $B_s$ such that $rf$ is $B_s$-periodic and $\psi(v_m) = 1$ on $B_s$, and let $c \neq 0$ be the constant of (i) for $B_s$. By (ii) there is a finite $R$ with $rf(v) = \sum_{x \in R} 1_{B_s}(v - x)\,rf(x)$. By (iii) choose $b_x$ with $rb_x = rf(x) \cdot 1_{B_s}$ for $x \in R$. Then $r(u(-x)b_x)(v) = 1_{B_s}(v - x)\,rf(x)$, so $r f = r\big(\sum_x u(-x)b_x\big)$ and, as $r$ is injective, $f = \sum_x u(-x)b_x$. Put $w = \sum_x \psi(-x_m)\,rf(x)$. Then
$$0 = Tf = \sum_{x \in R} \psi(-x_m)\, c\, rf(x) = c\,w,$$
so $w = 0$. The element $\sum_x \psi(-x_m) b_x$ has $r$-image $w \cdot 1_{B_s} = 0$, so it is $0$. Hence
$$f = \sum_{x \in R} \big(u(-x)b_x - \theta_\psi(u(-x))\,b_x\big) \in K.$$
So $\ker T = K$.

The map $T$ is onto: for $e \in E$ take $b$ with $rb = e \cdot 1_{B_s}$, and then $T(c^{-1}b) = e$. So $T$ induces a linear isomorphism from the coinvariants onto $E$. By the second property of $T$ it carries the action of $\iota(p)$, $p \in P_m$, to $\rho'(p)$. $\square$

**Theorem 1.6.5 (Induction from the whole group).** Let $\sigma$ be a smooth representation of a topological group $G$. Then $f \mapsto f(1)$ is an isomorphism $\operatorname{c-Ind}_G^G \sigma \cong \sigma$.

*Proof.* For $f$ in the induced space $f(g) = \sigma(g)f(1)$, so $f$ is determined by $f(1)$, and $g \mapsto \sigma(g)w$ lies in the space for every $w$ because $\sigma$ is smooth. The map commutes with the actions since $(g \cdot f)(1) = f(g) = \sigma(g)f(1)$. $\square$

**Lemma 1.6.6 (The rank zero computation).** In the setting of the theorem, $\Phi(\tau \times \sigma) \cong \operatorname{c-Ind}_{Q_{0,m}}^{P_m}\big((\Psi\tau)\nu^{m/2} \otimes \sigma|_{P_m}\big)$.

Lean: `GlobalTheory.CompanionTheory.MirLevi.comb_lem`.

*Proof.* Since $H_{1,m} = \iota(G_m)$ and $P_1$ is trivial, the twist $\tau\nu^{m/2}$ is trivial on $H_{1,m}$ and $\tau \times \sigma = \operatorname{c-Ind}_{G_m}^{P_{m+1}}\rho_0$ with $\rho_0 = 1_V \otimes \sigma\nu^{-1/2}$ on $V \otimes W$. By the theorem on $\Phi^-$ of an induction from $G_m$,
$$\Phi(\tau \times \sigma) = \Phi^-(\tau \times \sigma)\,\nu^{-1/2} \cong \nu \cdot \nu^{-1/2} \cdot \nu^{-1/2} \cdot (1_V \otimes \sigma|_{P_m}) = 1_V \otimes \sigma|_{P_m}.$$
The three twists cancel: $1 - \tfrac12 - \tfrac12 = 0$. On the other side $Q_{0,m} = P_m$, and the twist $\nu^{m/2}$ on the factor $G_0$ is trivial, so by the theorem on induction from the whole group the right side is also $1_V \otimes \sigma|_{P_m}$ on $V \otimes W$. $\square$

*Proof of the theorem.* The space of $\Psi\tau$ is $V$, since $U_1$ is trivial. By definition $\Psi\tau \times \sigma|_{P_m} = (\Psi\tau)\nu^{m/2} \mathbin{\times_0} \sigma|_{P_m}\nu^{0}$, which is the right side of the lemma. $\square$

The theorem holds for every continuous $\psi$, trivial or not: the proof never uses $\psi \neq 1$.

**Remark 1.6.7 (Formalization).** The rank zero theorem is in [PhiPgRankZeroHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PhiPgRankZeroHolds.lean#L645). There the group $P_n$ is `Mir k (n-1)`, so $\tau$ lies on `Mir k 0` and $\sigma$ on $\mathrm{GL}_{t+1}$ with $t + 1 = m$, and `PhiPG0` states the result with an index cast. The steps are `phiPG_zero` (L636), which removes the cast, `aux0` (L630), which passes from an isomorphism of twisted coinvariants to the isomorphism of mirabolic representations, and `comb_lem` (L620). The theorem on $\Phi^-$ of an induction from $G_m$ is `core` (L441) and `core0` (L425), with the kernel computed in `ker_eq` (L228). The facts $H_{1,m} = \iota(G_m)$ and $Q_{0,m} = P_m$ are `HPG_zero` (L276) and `mirabolicParabolic_zero_left_eq_top` (L308), and induction from the whole group is `cInd_top` (L372). The inputs (i), (ii) and (iii) are `restriction_ball_indicator_span`, `locally_constant_finite_ball_sum` and `exists_induced_ball_indicator`. Input (i) is called through a lemma at L114 named `exists_strictHenselian_absolutely_closed_local_ring`; the name has nothing to do with its statement. We opened the statements of the inputs, not their proofs, and the integral formula for $T$ above is a reason to believe (i), not its Lean proof. The statement assumes $\psi \neq 1$, but `phiPG0_holds` (L645) discards it. It does not assume $\tau$ smooth, which is automatic on the trivial group (`smooth_mirabolic_zero`, L489). The character $\nu$ is built from the normalized absolute value `nabs`, which we did not unfold.
