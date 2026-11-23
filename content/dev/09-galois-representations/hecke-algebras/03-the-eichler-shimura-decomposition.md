---
title: The Eichler and Shimura decomposition
decls:
  - GlobalTheory.HeckeFamilyMatrices.EichlerShimura.exists_per_add_cj_per
  - GlobalTheory.T.exists_eichlerShimura_decomposition_cocycle
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Eichler and Shimura decomposition

This section defines the group cohomology of a congruence subgroup with coefficients in polynomials of degree at most $w$, the period cocycle of a modular form, and the Hecke operators on cocycles. It proves that every cocycle is, up to a coboundary, the period of a modular form plus the complex conjugate of the period of a cusp form, in odd weight $k \geq 3$ and for $\Gamma$ between $\Gamma(M)$ and $\Gamma_1(N)$ with $N \geq 5$. This is the surjective half of the Eichler and Shimura isomorphism. It is used in [the semisimplicity theorem at a newform](/entry/hecke-semisimple-at-newform/), which reads Hecke eigenvalues on cocycles off the eigenvalues on modular forms.

**Definition 6.3.1 (Polynomial coefficients).** Let $w \geq 0$ and let $V_w = \mathbb{C}[X]_{\leq w}$ be the space of polynomials of degree at most $w$. For an integer matrix $g = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ put
$$
(P|g)(X) = (cX + d)^w \, P\!\left( \frac{aX + b}{cX + d} \right),
$$
that is, $X^i \mapsto (aX + b)^i (cX + d)^{w - i}$ extended linearly. On $V_w$ this is a right action of the monoid of integer matrices with nonzero determinant: $(P|g)|h = P|(gh)$.

**Definition 6.3.2 (Cocycles and coboundaries).** Let $\Gamma \leq \mathrm{SL}_2(\mathbb{Z})$. A *cocycle* is a map $z : \Gamma \to V_w$ with
$$
z(\gamma\delta) = z(\gamma)|\delta + z(\delta) \qquad (\gamma, \delta \in \Gamma).
$$
The cocycles form a complex vector space $Z^1(\Gamma, V_w)$. A *coboundary* is a cocycle of the form $\gamma \mapsto P|\gamma - P$ with $P \in V_w$. They form a subspace $B^1(\Gamma, V_w)$. The quotient is the group cohomology $H^1(\Gamma, V_w)$ for the right action.

**Definition 6.3.3 (Eichler integral and period cocycle).** Let $f$ be a modular form of weight $k = w + 2$ for $\Gamma$. Its *Eichler integral* is
$$
\mathcal{E}_f(\tau) = \int_i^\tau f(z)\,(X - z)^w \, dz \in V_w,
$$
taken along the segment from $i$ to $\tau$. Its *period cocycle* is $r_f(\gamma) = \mathcal{E}_f(\gamma i)|\gamma$ for $\gamma \in \Gamma$. For a map $z : \Gamma \to V_w$ let $\bar z(\gamma)$ be the polynomial $z(\gamma)$ with its coefficients conjugated.

The change of variables $z \mapsto \gamma z$ and the invariance $f|_k \gamma = f$ give $\mathcal{E}_f(\gamma\tau)|\gamma = \mathcal{E}_f(\tau) + r_f(\gamma)$ for all $\tau \in \mathcal{H}$. From this the cocycle law follows:
$$
\begin{aligned}
r_f(\gamma\delta) &= \bigl(\mathcal{E}_f(\gamma(\delta i))|\gamma\bigr)\big|\delta \\
&= \bigl(\mathcal{E}_f(\delta i) + r_f(\gamma)\bigr)\big|\delta = r_f(\delta) + r_f(\gamma)|\delta.
\end{aligned}
$$
So $r_f \in Z^1(\Gamma, V_w)$. The map $f \mapsto r_f$ is $\mathbb{C}$-linear, and $z \mapsto \bar z$ maps cocycles to cocycles and coboundaries to coboundaries, since the matrices have integer entries.

**Definition 6.3.4 (Hecke operators on cocycles).** Let $\delta_1, \dots, \delta_m$ be integer matrices with positive determinant. For $z : \Gamma \to V_w$ and $\gamma \in \Gamma$, suppose there are a permutation $\pi$ of $\{1, \dots, m\}$ and elements $\gamma'_i \in \Gamma$ with $\delta_i \gamma = \gamma'_i \delta_{\pi(i)}$ for all $i$. Then put
$$
(T_\delta z)(\gamma) = \sum_{i=1}^m z(\gamma'_i)\,|\,\delta_{\pi(i)}.
$$
If no such $\pi$ exists, put $(T_\delta z)(\gamma) = 0$. For a family $\delta$ that represents a double coset $\Gamma \alpha \Gamma$, the permutation always exists, and $T_\delta$ is the usual Hecke operator on group cohomology.

For $\Gamma = \Gamma_1(N) \cap \Gamma_0(l)$, $q$ a prime and $\sigma \in \Gamma_0(Nl)$ with lower right entry $\equiv q \pmod N$, we use three families:
$$
\begin{aligned}
T_q &: \begin{pmatrix} 1 & i \\ 0 & q \end{pmatrix} \ (0 \leq i < q), \quad \sigma \begin{pmatrix} q & 0 \\ 0 & 1 \end{pmatrix}, \\
U_l &: \begin{pmatrix} 1 & j \\ 0 & l \end{pmatrix} \ (0 \leq j < l), \\
\langle d \rangle &: \sigma_d, \text{ one matrix in } \Gamma_0(Nl) \text{ with lower right entry} \equiv d \pmod N.
\end{aligned}
$$
The same families act on functions on $\mathcal{H}$ by $f \mapsto \sum_i f|_k \delta_i$, with the slash operator $f|_k g = (\det g)^{k - 1}(c\tau + d)^{-k} f(g\tau)$. These are the Hecke operators $T_q$, $U_l$ and the diamond operators on [modular forms](/learn/automorphic-forms/#modular-forms); with this normalisation the coefficient of $q^n$ in $\sum_i f|_k \delta_i$ for the $U_l$ family is the coefficient of $q^{ln}$ in $f$.

**Theorem 6.3.5 (Eichler and Shimura decomposition).** Let $N \geq 5$ and $M \geq 1$, let $\Gamma(M) \leq \Gamma \leq \Gamma_1(N)$, let $k \geq 3$ be odd, and let $w = k - 2$. Then for every cocycle $z \in Z^1(\Gamma, V_w)$ there are $f \in M_k(\Gamma)$ and $h \in S_k(\Gamma)$ with
$$
z - r_f - \overline{r_h} \in B^1(\Gamma, V_w).
$$

Lean: `GlobalTheory.HeckeFamilyMatrices.EichlerShimura.exists_per_add_cj_per` (also `GlobalTheory.T.exists_eichlerShimura_decomposition_cocycle`, a second name).

*Proof.* Consider the map
$$
\Phi : M_k(\Gamma) \times S_k(\Gamma) \to Z^1(\Gamma, V_w)/B^1(\Gamma, V_w), \qquad (f, h) \mapsto r_f - \overline{r_h}.
$$
It is additive and $\mathbb{R}$-linear, but not $\mathbb{C}$-linear, since $\overline{r_{ch}} = \bar c\,\overline{r_h}$. We show that $\Phi$ is injective and that the real dimensions match.

*Injectivity.* Let $r_f - \overline{r_h} \in B^1$. A first lemma shows that $f$ is then a cusp form: the cocycle $r_f$ restricted to the stabiliser of each cusp detects the constant term of $f$ there. A second lemma shows that $f = h = 0$ when $f, h$ are cusp forms and $r_f - \overline{r_h}$ is a coboundary. Its proof is the positivity of the Petersson product: the cup product of the classes of $r_f$ and $\overline{r_f}$ is a nonzero multiple of $\langle f, f \rangle$, and it pairs to zero with a coboundary. See [the Petersson inner product](/learn/automorphic-forms/#modular-forms).

*Dimensions.* Since $N \geq 5$, the group $\Gamma$ has no torsion and does not contain $-1$. Its image in $\mathrm{PSL}_2(\mathbb{Z}) \cong \mathbb{Z}/2 * \mathbb{Z}/3$ is then a free group of rank $1 + [\mathrm{SL}_2(\mathbb{Z}) : \Gamma]/12$, by the Kurosh subgroup theorem and the Euler characteristic $-1/6$ of $\mathrm{PSL}_2(\mathbb{Z})$. A cocycle on a free group is fixed by its values on the generators, so
$$
12 \dim_{\mathbb{C}} Z^1(\Gamma, V_w) \leq (w + 1)\bigl(12 + [\mathrm{SL}_2(\mathbb{Z}) : \Gamma]\bigr).
$$
A polynomial fixed by $\Gamma(M)$ under the slash action is $0$ when $w \geq 1$, as $\Gamma(M)$ contains a unipotent and a lower unipotent element. So $P \mapsto (\gamma \mapsto P|\gamma - P)$ is injective and $\dim B^1 = w + 1$. Hence
$$
12 \dim_{\mathbb{C}} (Z^1/B^1) \leq (w + 1)[\mathrm{SL}_2(\mathbb{Z}) : \Gamma] = (k - 1)[\mathrm{SL}_2(\mathbb{Z}) : \Gamma].
$$
By [the odd weight dimension bound](/entry/dim-lower-bound/), the right side is at most $12(\dim M_k(\Gamma) + \dim S_k(\Gamma))$. So $\dim_{\mathbb{R}}(Z^1/B^1) \leq \dim_{\mathbb{R}}(M_k(\Gamma) \times S_k(\Gamma))$.

*Conclusion.* An injective $\mathbb{R}$-linear map from a finite dimensional real space to a space of at most the same dimension is surjective. So for $z \in Z^1$ there is $(f, h')$ with $z - r_f + \overline{r_{h'}} \in B^1$, and $h = -h'$ gives the claim. $\square$

Taken together with the injectivity in the proof, the theorem says that $M_k(\Gamma) \oplus \overline{S_k(\Gamma)} \to H^1(\Gamma, V_w)$ is an isomorphism. This is the Eichler and Shimura isomorphism (G. Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Chapter 8). Here it is proved only for odd weight and for $\Gamma \leq \Gamma_1(N)$ with $N \geq 5$, and only the surjective half is stated.

**Remark 6.3.6 (Formalization).** The statement with the second name is a wrapper of the first under `maxHeartbeats 1000000`. The Hecke operator on cocycles is defined to be $0$ at $\gamma$ when no permutation $\pi$ exists ([IsDCReps.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/IsDCReps.lean#L42)). The diamond family uses $\sigma \in \Gamma_0(Nl)$ ([IsDCReps.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/IsDCReps.lean#L53)), while the operators on the Kummer module of later sections use $\Gamma_0(N) \cap \Gamma_0(l)$. The positivity lemma, the cuspidality lemma and the bound on cocycles were read as statements; the arguments given above are the classical ones.
