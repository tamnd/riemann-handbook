---
title: Decay of matrix coefficients
decls:
  - ReciprocityTheory.ChartRestriction.DS.DecInf.decSmJ
  - ReciprocityTheory.ChartRestriction.DS.DecInf.decSm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Decay of matrix coefficients

Matrix coefficients of a discrete series representation are square integrable by definition. Many arguments need more: a bound that decays like a fixed power of the size of $g$, uniform in the vectors, with a constant controlled by finitely many derivatives of the vectors. This section proves such a bound for discrete series of $U(p,q)$ whose Harish-Chandra parameter has a large gap. The decay order $m$ can be as large as the gap allows. We prove it first for the standard form $G_\varepsilon$ of $U(p,q)$, and then for the form of $U(k+r, r+1)$ that is preserved by a Hermitian matrix with $r$ hyperbolic planes. The second form is used in the step [the hypotheses are not empty](/step/nonempty-hyps/).

Background: [asymptotics of matrix coefficients](/learn/real-groups/#asymptotics-of-matrix-coefficients), [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees), [[unitary representation|74BPYJNZTM]].

### Notation

We keep the notation of the previous sections: $\varepsilon$, $p$, $q$, $n = p+q$, $q_0 = \min(p,q)$, the groups $G_\varepsilon$ and $K_\varepsilon$, the threshold $\theta_\varepsilon = \max(npq+1, 16nq_0 + 8\sqrt{2q_0})$, gaps, Harish-Chandra parameters and discrete series of parameter $\lambda$ (see [Theorem 3.5.6](/entry/sup-trace/)). For a matrix $g$ put
$$\|g\|_{\mathrm{HS}} = \Bigl(\sum_{a,b}|g_{ab}|^2\Bigr)^{1/2}.$$
On $G_\varepsilon$ this is at least $\sqrt{n}$, with equality exactly on $K_\varepsilon$, and it grows like the largest singular value of $g$.

Let $\sigma$ be a map from $M_n(\mathbb{C})$ to bounded operators on a Hilbert space $H$. A vector $v \in H$ is *smooth* if $g \mapsto \sigma(g)v$ is smooth on $G_\varepsilon$, in the sense that near every point of $G_\varepsilon$ it agrees on $G_\varepsilon$ with a smooth function on an open set of $M_n(\mathbb{C})$. For a matrix $X$ and $v \in H$ put
$$d\sigma(X)v = \frac{d}{dt}\Big|_{t=0} \sigma(\exp tX)v,$$
and for a word $w = (X_1, \dots, X_l)$ put $d\sigma(w)v = d\sigma(X_1)\cdots d\sigma(X_l)v$, with $d\sigma(\emptyset)v = v$. For a finite list $\mathcal{W}$ of words put
$$\nu_{\mathcal{W}}(v) = \sum_{w \in \mathcal{W}} \|d\sigma(w)v\|.$$

**Definition 3.6.1 (Decay bound).** Let $m, N \in \mathbb{N}$. We say that $\sigma$ satisfies the *decay bound of order $m$ with $N$ derivatives* if there are a constant $C$ and a finite list $\mathcal{W}$ of words with the following properties: every word in $\mathcal{W}$ has length at most $N$ and has all its letters in the Lie algebra of $G_\varepsilon$; and for all smooth $u, v \in H$ and all $g \in G_\varepsilon$,
$$\|g\|_{\mathrm{HS}}^{\,m}\, |\langle v, \sigma(g)u\rangle| \leq C\, \nu_{\mathcal{W}}(u)\, \nu_{\mathcal{W}}(v).$$

### The standard form

**Theorem 3.6.2 (Decay of discrete series matrix coefficients).** Let $\lambda$ be a Harish-Chandra parameter with gap at least $h$, and let $m \in \mathbb{N}$ with $\theta_\varepsilon + m < h$. Let $H$ be complete and let $\sigma$ be a discrete series of parameter $\lambda$ on $H$. Then $\sigma$ satisfies the decay bound of order $m$ with $m(n-1)$ derivatives.

Lean: `ReciprocityTheory.ChartRestriction.DS.DecInf.decSmJ`.

*Proof.* First let $p = 0$ or $q = 0$. Then $G_\varepsilon = U(n)$, so $\|g\|_{\mathrm{HS}}^2 = n$ for every $g \in G_\varepsilon$, since every column of a unitary matrix has length $1$. Take $\mathcal{W}$ to be the list that contains only the empty word, so that $\nu_{\mathcal{W}}(v) = \|v\|$, and take $C = \sqrt{n}^{\,m}$. The bound follows from the Cauchy-Schwarz inequality and $\|\sigma(g)u\| = \|u\|$.

Now let $p, q \geq 1$, so $q_0 \geq 1$. The inequality $\theta_\varepsilon + m < h$ gives $\theta_\varepsilon < h$, and since $\theta_\varepsilon \geq 16 n q_0 + 8\sqrt{2q_0}$ it also gives $8 n q_0 < h$. Fix a $K$-type $T$ of highest weight $\Lambda_K(\lambda)$ and a nonzero vector $v_0$ in it. By the results of the section on Gelfand invariants there is a function $\Psi$ on $G_\varepsilon$ with values in the endomorphisms of $T$ with these properties: $\Psi(k_1 g k_2) = T(k_1)\Psi(g)T(k_2)$ for $k_1, k_2 \in K_\varepsilon$; $\Psi(1) = 1$; $\Psi$ is smooth; the Casimir operator acts on $\Psi$ by the scalar $c(\lambda) = |\lambda|^2 - |\rho|^2$; $\Psi$ is square integrable for every Haar measure; and
$$\|\Psi(k \exp X)\| \leq \exp\Bigl(-\frac{h}{8}\min\Bigl(\|X\|_{\mathrm{HS}}^2,\ \frac{\|X\|_{\mathrm{HS}}}{\sqrt{2q_0}}\Bigr)\Bigr)$$
for $k \in K_\varepsilon$ and $X$ in the noncompact part $\mathfrak{p}$ of the Lie algebra.

For $v \in T$ the function $g \mapsto \langle v_0, \Psi(g)v\rangle$ is in $L^2(G_\varepsilon)$. Let $V_\Psi$ be the set of smooth vectors in the span of these functions, let $H_\lambda$ be the closure of the space generated by $V_\Psi$ under the Lie algebra, and let $\sigma_\lambda(g)$ be the right regular representation $R(g)$ followed by the orthogonal projection onto $H_\lambda$. The core estimate is an induction on $m$: there is $C$ such that for all $x, y$ in the generated space, all $g \in G_\varepsilon$ and all choices of $m$ index pairs $(a_t, b_t)$,
$$|\langle y, R(g)x\rangle| \prod_{t=1}^m |g_{a_tb_t}| \leq C\, N(x)\, N(y),$$
where $R$ is the right regular representation and $N(x)$ is the sum of the norms of $E_{a_1b_1}\cdots E_{a_lb_l}x$ over all words of length $l \leq m(n-1)$. This induction uses the gap hypothesis $\theta_\varepsilon + m < h$. Next, for $c \geq 0$, if $c\prod_t |g_{a_tb_t}| \leq A$ for every choice of the pairs, then
$$\|g\|_{\mathrm{HS}}^{\,m}\, c \leq n^{2m} A,$$
since $\|g\|_{\mathrm{HS}}^{\,m} \leq n^m \max_{a,b}|g_{ab}|^m$ and the maximum is reached for one choice of pairs. With $c = |\langle y, R(g)x\rangle|$ and $A = C\,N(x)N(y)$ we get the bound of order $m$ for the generated space, with constant $n^{2m}C$. The model representation $\sigma_\lambda$ then satisfies the decay bound of order $m$ with $m(n-1)$ derivatives. Finally the bound passes from $\sigma_\lambda$ to the given discrete series $\sigma$ of parameter $\lambda$. $\square$

### The Hermitian form with hyperbolic planes

Let $k, r \in \mathbb{N}$ and $N' = 2r + k + 1$, with indices $0, \dots, N'-1$. Let $H_{k,r}$ be the $N' \times N'$ matrix with:

- entry $1$ at $(i,j)$ when $i + j = 2r + k$ and $i < r$ or $j < r$;
- entry $1$ at $(i,i)$ for $r \leq i < r + k$, and entry $-1$ at $(r+k, r+k)$;
- entry $0$ elsewhere.

So $H_{k,r}$ is the sum of $r$ hyperbolic planes and the diagonal form $\operatorname{diag}(1, \dots, 1, -1)$ on the $k+1$ middle coordinates, and its signature is $(k+r, r+1)$. Let $U(H_{k,r})$ be the group of $g$ with $g^* H_{k,r} g = H_{k,r}$, and let its Lie algebra be the set of $X$ with $X^* H_{k,r} + H_{k,r} X = 0$. A *unitary Cayley matrix* for $\varepsilon \in \{+,-\}^{N'}$ is an invertible unitary matrix $P$ with $P^* J_\varepsilon P = H_{k,r}$. Then $g \mapsto P g P^{-1}$ maps $U(H_{k,r})$ onto $G_\varepsilon$.

Let $\sigma$ be a map from $M_{N'}(\mathbb{C})$ to bounded operators on $H$. We say that $\sigma$ is a *discrete series of parameter $\lambda$ for $H_{k,r}$* if there is a unitary Cayley matrix $P$ for $\varepsilon$ such that $g \mapsto \sigma(P^{-1}gP)$ is a discrete series of parameter $\lambda$ for $G_\varepsilon$. Smooth vectors and $d\sigma$ are defined as above, with $U(H_{k,r})$ in place of $G_\varepsilon$.

**Theorem 3.6.3 (Decay for the form with hyperbolic planes).** Let $\varepsilon \in \{+,-\}^{2r+k+1}$, let $\lambda$ be a Harish-Chandra parameter with gap at least $h$ for $\varepsilon$, and let $m \in \mathbb{N}$ with $\theta_\varepsilon + m < h$. Let $H$ be complete and let $\sigma$ be a discrete series of parameter $\lambda$ for $H_{k,r}$. Then there are a constant $C$ and a finite list $\mathcal{W}$ of words with these properties: every word has length at most $m(2r+k)$ and has all its letters in the Lie algebra of $U(H_{k,r})$; and for all smooth $u, v$ and all $g \in U(H_{k,r})$,
$$\|g\|_{\mathrm{HS}}^{\,m}\, |\langle v, \sigma(g)u\rangle| \leq C\, \nu_{\mathcal{W}}(u)\, \nu_{\mathcal{W}}(v).$$

Lean: `ReciprocityTheory.ChartRestriction.DS.DecInf.decSm`.

*Proof.* Let $P$ be the unitary Cayley matrix of the hypothesis, and $\sigma'(g) = \sigma(P^{-1}gP)$. By [Theorem 3.6.2](/entry/dec-sm-j/) with $n = 2r+k+1$, the representation $\sigma'$ of $G_\varepsilon$ satisfies the decay bound of order $m$ with $m(n-1) = m(2r+k)$ derivatives. Transport this bound along $g \mapsto P^{-1}gP$. Since $P$ is unitary, $\|P^{-1}gP\|_{\mathrm{HS}} = \|g\|_{\mathrm{HS}}$. The conjugate $P^{-1}XP$ of an element $X$ of the Lie algebra of $G_\varepsilon$ is in the Lie algebra of $U(H_{k,r})$, and $\exp(tP^{-1}XP) = P^{-1}\exp(tX)P$, so the words of $\mathcal{W}$ transport to words of the same length. Smooth vectors for $\sigma$ on $U(H_{k,r})$ are smooth for $\sigma'$ on $G_\varepsilon$, because conjugation by $P$ is linear. $\square$

The decay theorem is an explicit form of a classical fact: $K$-finite matrix coefficients of discrete series lie in the Harish-Chandra Schwartz space, so they decay faster than any power of $\|g\|$ when the parameter is far from the walls (Harish-Chandra; see the notes at the end of the chapter). Here only a finite order $m$ is reached, and the order is limited by the gap.

**Remark 3.6.4 (Formalization).** In the first theorem the compact case $p = 0$ or $q = 0$ is handled by a separate argument, before the main proof ([DecBoundOfCompact.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/InfinitesimalDecay/DecBoundOfCompact.lean#L84)). The second theorem states its hypotheses with the copies of the gap condition and of Harish-Chandra parameters from the general notation, while the first uses the copies of the discrete series development; the proof converts between them. The operator $\sigma(g)$ is defined for all matrices, and only its values on the group matter. We opened the statements of the induction on $m$, of the inequality for $\|g\|_{\mathrm{HS}}^m$, of the existence of $\Psi$ and of the two transfer lemmas, but not their proofs. In particular we have not checked how the passage from the model $\sigma_\lambda$ to $\sigma$ uses the discrete series hypothesis.
