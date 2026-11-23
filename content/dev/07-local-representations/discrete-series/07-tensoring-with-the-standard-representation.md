---
title: Tensoring with the standard representation
decls:
  - ReciprocityTheory.ChartRestriction.DS.cc_gk
  - ReciprocityTheory.ChartRestriction.DS.G2.cc_gk
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Tensoring with the standard representation

Let $\pi_\lambda$ be the discrete series of $U(p,q)$ with Harish-Chandra parameter $\lambda$. If one coordinate of $\lambda$ moves by $\pm 1$, the new discrete series $\pi_{\lambda \pm e_s}$ is a summand of $\pi_\lambda$ tensored with the standard representation $\mathbb{C}^n$ or its dual. This section proves this inside the space of smooth vectors of $L^2(U(p,q))$, identifies the summand as an eigenspace of one explicit operator, and computes the ratio of formal degrees:
$$\frac{d(\pi_{\lambda + e_s})}{d(\pi_\lambda)} = \prod_{s' \neq s} \frac{\lambda_s + 1 - \lambda_{s'}}{\lambda_s - \lambda_{s'}}.$$
The result is used in the step [the local theta matching](/step/theta-local-matching/), and in a second version with a different gap threshold in the step [EveryCharacter from the literature](/step/every-character-of-literature/).

Background: [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees), [the Casimir operator](/learn/real-groups/#the-center-of-umathfrakg-and-the-casimir-operator), [highest weights](/learn/representations/#highest-weights-and-branching), [[irreducible representation|FX3NEFYFFN]].

### The model representations

We keep the notation of the previous sections: $\varepsilon$, $n = p + q$, $q_0 = \min(p,q)$, $G_\varepsilon$, $K_\varepsilon$, the weights $\rho$, $\Lambda_K(\lambda)$, $c(\lambda)$, gaps and the threshold $\theta_\varepsilon$ ([Theorem 3.5.6](/entry/sup-trace/)), and the Gelfand operators $\Gamma_k$ and their eigenvalues $\gamma_k(\ell(\lambda))$ with $\ell(\lambda)_r = \lambda_r + (n-1)/2$ ([Theorem 3.4.9](/entry/psi-m-gelfand/)). For operators $E_{ab}$ put $E^\vee_{ab} = -E_{\bar b \bar a}$, where $\bar a = n - 1 - a$ with indices from $0$.

Let $R$ be the right regular representation of $G_\varepsilon$ on $L^2(G_\varepsilon)$, for the Haar measure $dg$ of the general notation. Let $D$ be its space of smooth vectors, with the derived action $E_{ab}$. A weight $\lambda$ satisfies the *standard gap condition* if it is strictly decreasing and has gap at least $h$ for some $h > npq + 1$.

**Definition 3.7.1 (Model datum).** Let $\lambda$ satisfy the standard gap condition and let $T$ be a $K$-type of highest weight $\Lambda_K(\lambda)$. A *spherical function for $(\lambda, T)$* is a function $\Psi$ from $M_n(\mathbb{C})$ to the endomorphisms of $T$ such that: $\Psi(k_1gk_2) = T(k_1)\Psi(g)T(k_2)$ for $k_1, k_2 \in K_\varepsilon$ and $g \in G_\varepsilon$; $\Psi(1) = 1$; $\Psi$ is smooth on $G_\varepsilon$; the Casimir operator acts on $\Psi$ by $c(\lambda)$; and $\Psi$ is square integrable on $G_\varepsilon$ for every Haar measure. For such $\Psi$ and $v_0 \in T$, $v_0 \neq 0$, let:

- $V_\Psi \subseteq D$ be the set of smooth vectors in the span of the functions $g \mapsto \langle v_0, \Psi(g)v\rangle$, $v \in T$;
- $M_\Psi = U(\mathfrak{g})V_\Psi$ be the generated subspace;
- $H_\Psi$ be the closure of $M_\Psi$ in $L^2(G_\varepsilon)$;
- $\sigma_\Psi(g)$ be $R(g)$ followed by the orthogonal projection onto $H_\Psi$.

**Definition 3.7.2 (Formal degree).** For a map $\sigma$ from matrices to operators on $H$ and $w \in H$, put
$$d(\sigma, w) = \frac{\|w\|^4}{\int_{G_\varepsilon} |\langle w, \sigma(g)w\rangle|^2\, dg}.$$
If $\sigma$ is irreducible and square integrable, the Schur orthogonality relations give $\int |\langle w, \sigma(g)w\rangle|^2\,dg = \|w\|^4/d_\sigma$, so $d(\sigma, w)$ is the formal degree $d_\sigma$ for every $w \neq 0$.

### Tensor products with $\mathbb{C}^n$

Let $\delta \in \{0, 1\}$; $\delta = 0$ stands for the standard representation and $\delta = 1$ for its dual. On $D^n = D \otimes \mathbb{C}^n$, written as vectors $f = (f_1, \dots, f_n)$, define for $\delta = 0$
$$(E^{(0)}_{ab}f)_c = E_{ab}f_c + \delta_{ca}f_b, \qquad (\mathcal{E}^{(0)}f)_s = \sum_r E_{rs}f_r,$$
and for $\delta = 1$
$$(E^{(1)}_{ab}f)_c = E_{ab}f_c - \delta_{cb}f_a, \qquad (\mathcal{E}^{(1)}f)_r = -\sum_s E_{rs}f_s.$$
For $k \in K_\varepsilon$ let $k^{(0)}$ act by $(k^{(0)}f)_c = \sum_d k_{cd}\,R(k)f_d$ and $k^{(1)}$ by the same formula with $\overline{k_{cd}}$. Put
$$\lambda^{(0)} = \lambda + e_s, \quad \lambda^{(1)} = \lambda - e_s, \quad z^{(0)}_s = \lambda_s + \frac{1-n}{2}, \quad z^{(1)}_s = -\lambda_s + \frac{1-n}{2},$$
$$r^{(0)}_s(\lambda) = \prod_{s' \neq s}\frac{\lambda_s + 1 - \lambda_{s'}}{\lambda_s - \lambda_{s'}}, \qquad r^{(1)}_s(\lambda) = \prod_{s' \neq s}\frac{\lambda_s - 1 - \lambda_{s'}}{\lambda_s - \lambda_{s'}}.$$

**Definition 3.7.3 (Equivariant embedding).** A linear map $\iota : D \to D^n$ is an *equivariant embedding of $M'$ into $M^n$ of type $\delta$* if: $\iota(M') \subseteq M^n$; $\iota$ is injective on $M'$; $\iota(E_{ab}x) = E^{(\delta)}_{ab}\iota(x)$ for $x \in M'$; and $\iota(R(k)x) = k^{(\delta)}\iota(x)$ for $k \in K_\varepsilon$ and $x \in M'$ with $R(k)x \in M'$.

### The theorem

The hypotheses on a pair $(\lambda, \Psi)$ are: $\lambda$ satisfies the standard gap condition, has gap at least $h$ and $\theta_\varepsilon < h$; $\Psi$ is a spherical function for $(\lambda, T)$ and $v_0 \neq 0$; $\Psi(\exp X)$ is a positive operator for every $X$ in the noncompact part $\mathfrak{p}$ of the Lie algebra; for all $v, w \in M_\Psi$ the function $g \mapsto \|g\|_{\mathrm{HS}}\,\langle w, R(g)v\rangle$ is in $L^2(G_\varepsilon)$; and $M_\Psi$ has *Gelfand character $\lambda$*: $\Gamma_k x = \gamma_k(\ell(\lambda))x$ and $\Gamma^\vee_k x = \gamma_k(\ell(-\lambda))x$ for all $k \geq 0$ and $x \in M_\Psi$, where $\Gamma^\vee_k$ is built from the reversed operators $E^\vee$.

**Theorem 3.7.4 (Tensoring a discrete series with the standard representation).** Let $\delta \in \{0,1\}$ and $s \in \{1, \dots, n\}$. Let $(\lambda, \Psi)$ and $(\lambda', \Psi')$ satisfy the hypotheses above, with $\lambda' = \lambda^{(\delta)}$. Let $w \in H_\Psi$ and $w' \in H_{\Psi'}$ be nonzero. Then:

1. there is an equivariant embedding $\iota$ of $M_{\Psi'}$ into $M_\Psi^n$ of type $\delta$ such that $\mathcal{E}^{(\delta)}\iota(x) = z^{(\delta)}_s\,\iota(x)$ for all $x \in M_{\Psi'}$, and every $f \in M_\Psi^n$ with $\mathcal{E}^{(\delta)}f = z^{(\delta)}_s f$ is $\iota(x)$ for some $x \in M_{\Psi'}$;
2. the formal degrees satisfy
$$\frac{d(\sigma_{\Psi'}, w')}{d(\sigma_\Psi, w)} = r^{(\delta)}_s(\lambda).$$

Lean: `ReciprocityTheory.ChartRestriction.DS.cc_gk`.

*Proof.* The model $\sigma_\Psi$ is square integrable, and its formal degree $d(\sigma_\Psi, w)$ is positive for $w \neq 0$; the same holds for $\Psi'$. An equivariant embedding $\iota$ of $M_{\Psi'}$ into $M_\Psi^n$ of type $\delta$ exists, and its image lies in the $z^{(\delta)}_s$-eigenspace of $\mathcal{E}^{(\delta)}$. Next there is an operator $P$ on $D^n$ which commutes with $K$ and the Lie algebra on $M_\Psi^n$, is idempotent and symmetric for the natural form on $M_\Psi^n$, has image in the $z^{(\delta)}_s$-eigenspace, and is the identity there. Its partial trace over $\mathbb{C}^n$ acts on $M_\Psi$ by a scalar $c$, and the pole computation gives $c = r^{(\delta)}_s(\lambda)$. Since $P\iota(x) = \iota(x)$, the comparison of traces gives
$$\frac{d(\sigma_{\Psi'}, w')}{d(\sigma_\Psi, w)} \leq r^{(\delta)}_s(\lambda),$$
and, in the case of equality, every $Pf$ with $f \in M_\Psi^n$ is in the image of $\iota$.

Now exchange the roles. Since $\lambda = (\lambda')^{(1-\delta)}$, the same argument with $1 - \delta$ gives
$$\frac{d(\sigma_\Psi, w)}{d(\sigma_{\Psi'}, w')} \leq r^{(1-\delta)}_s(\lambda').$$
A direct computation gives $r^{(\delta)}_s(\lambda)\, r^{(1-\delta)}_s(\lambda') = 1$: for $\delta = 0$ the factors are $(\lambda_s + 1 - \lambda_{s'})/(\lambda_s - \lambda_{s'})$ and $(\lambda_s - \lambda_{s'})/(\lambda_s + 1 - \lambda_{s'})$, and both $\lambda$ and $\lambda'$ are injective by the gap condition. If $a, b > 0$, $a/b \leq r$, $b/a \leq r_2$ and $r r_2 = 1$, then $a/b = r$. So item 2 holds with equality, and the equality case gives the surjectivity in item 1, since $Pf = f$ for every $f$ in the eigenspace. $\square$

When the shifted weight is not injective, the ratio is zero: if $\lambda^{(\delta)}_s = \lambda_{s'}$ for some $s' \neq s$, one factor of $r^{(\delta)}_s(\lambda)$ vanishes. Such a $\lambda^{(\delta)}$ is not strictly decreasing, so the theorem does not apply to it.

### The second threshold

Put
$$\theta'_\varepsilon = \max\bigl(2n,\ 16nq_0 + 8\sqrt{2q_0}\bigr).$$
A weight satisfies the *weak gap condition* if it is strictly decreasing and has gap at least $h$ for some $h > 2n$.

**Theorem 3.7.5 (Tensoring with the second threshold).** The previous theorem holds with the standard gap condition replaced by the weak gap condition, and $\theta_\varepsilon$ replaced by $\theta'_\varepsilon$, in the hypotheses on both pairs.

Lean: `ReciprocityTheory.ChartRestriction.DS.G2.cc_gk`.

*Proof.* The proof has the same steps as the proof of [Theorem 3.7.4](/entry/ds-cc-gk/): construct the embedding, construct the projection $P$ onto the eigenspace, compute its partial trace, compare traces in both directions, and use $r^{(\delta)}_s(\lambda)\, r^{(1-\delta)}_s(\lambda') = 1$. Each auxiliary result is replaced by a version proved under the weak gap condition and the threshold $\theta'_\varepsilon$. $\square$

If $p, q \geq 1$, then $16nq_0 + 8\sqrt{2q_0} > 2n$, so $\theta'_\varepsilon \leq \theta_\varepsilon$, with strict inequality when $npq + 1$ is the larger term of $\theta_\varepsilon$. So the second theorem needs no larger gap than the first. The value of the ratio agrees with the formula of Harish-Chandra for the formal degree, which is proportional to $\prod_{a<b}|\lambda_a - \lambda_b|$ (see the notes at the end of the chapter).

**Remark 3.7.6 (Formalization).** The second theorem is in a folder named after the exceptional group $G_2$, but it is about $U(p,q)$, like the first. Its statement differs from the first only in the threshold $\theta'_\varepsilon$ and in the gap condition, which is the copy of the standard gap condition with $2n$ in place of $npq + 1$ ([CcARatioZero.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/ExceptionalGroupG2/TensorProductsG2/CcARatioZero.lean#L85), compared with [CcARatioZero.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TensorRepresentations/CcARatioZero.lean#L82)). In both theorems the gap condition on $\lambda$ and $\lambda'$ follows from the other hypotheses, since a gap $h > \theta_\varepsilon \geq npq + 1$ (or $h > \theta'_\varepsilon \geq 2n$) is already assumed; only the strict decrease is new. Both theorems state the formal degree through $d(\sigma, w)$ for one vector, not through a formal degree of the representation. We opened the statements of the existence of $\iota$ and of the trace comparison, but not their proofs, and we did not open the construction of $P$ or the pole computation.
