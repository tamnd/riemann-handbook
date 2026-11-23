---
title: The rank one transfer
decls:
  - GlobalTheory.JR.RankOneTransfer.rankOne
  - GlobalTheory.T.etaleOrbitalFourier_rankOne_transfer
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The rank one transfer

After a descent to the centralizer, a regular orbit of the Jacquet-Rallis action becomes an orbit of a torus on a space of rank one over an etale algebra $K$. On the linear side, $K^\times$ acts on $K \times K$; on the Hermitian side, the norm one group of $L = K \otimes_F E$ acts on $L$. This section proves that the Fourier transform preserves matching for these rank one orbital integrals, up to the Weil constant. The tool is the induced representation of $\mathrm{SL}_2(K)$ and a uniqueness statement for its Whittaker functionals. The result is used in [the proof of Fourier matching](/entry/fourier-match-at-of-weil/).

Throughout, $(F, E)$ is an unramified quadratic pair, $(K, L)$ an etale Hermitian pair over it, and $\psi$ a standard character of $F$, with the notation $|\cdot|_K$, $\eta_K$, $\psi_K$, $N$ and $B_x$ of [the previous section](/entry/weil-field-main/). In this section a unit of a ring means an invertible element. Let $U(L) = \{ t \in L : t \bar t = 1 \}$.

**Definition 4.3.1 (Rank one orbital integrals).** Let $\mu_K$ be a Haar measure on $K$ and $\nu$ a Haar measure on $U(L)$. For a function $\varphi'$ on $K \times K$, a function $\varphi$ on $L$, $a \in K$ and $y_0 \in L$ put
$$O_K(\varphi', a) = \int_{K^\times} \varphi'(a t^{-1}, t)\, \eta_K(t)\, |t|_K^{-1}\, d\mu_K(t), \qquad O_L(\varphi, y_0) = \int_{U(L)} \varphi(t y_0)\, d\nu(t).$$

The group $K^\times$ acts on $K \times K$ by $t \cdot (b, c) = (t^{-1} b, t c)$, with invariant $bc$. The first integral runs over the orbit of $(a, 1)$ with the $\eta_K$-twisted multiplicative Haar measure $|t|_K^{-1} d\mu_K$. The second is the orbital integral of $U(L)$ acting on $L$, with invariant $N(y)$.

**Definition 4.3.2 (Rank one measures).** A choice of rank one measures is a measure $\mu_K$ on $K$, a measure $\mu_{L, x}$ on $L$ for each $x \in K^\times$, and a measure $\nu$ on $U(L)$, such that: $\mu_K$ is self-dual for the kernel $\psi_K(y y')$; each $\mu_{L, x}$ is self-dual for $B_x$; $\nu$ is a Haar measure; and for every map $s : K \to L$ with $N(s(N(y))) = N(y)$ for all units $y$, and every test function $h$ on $L$ with support in the units,
$$\int_L h(y)\, |N(y)|_K^{-1}\, d\mu_{L,1}(y) = \int_{N(L^\times)} O_L\big(h, s(a)\big)\, |a|_K^{-1}\, d\mu_K(a).$$

The last condition is the integration formula for the fibration $N : L^\times \to N(L^\times)$, whose fibres are the orbits of $U(L)$.

**Definition 4.3.3 (Representatives).** A set $S \subset K^\times$ is a set of representatives if every $a \in K^\times$ can be written $a = x N(y)$ with $x \in S$ and $y \in L^\times$, and the element $x$ is unique.

So $S$ maps bijectively to $K^\times / N(L^\times)$. This group is finite.

**Definition 4.3.4 (Induced functions).** A function $\Phi$ on $\mathrm{SL}_2(K)$ is induced if there is a neighbourhood $U$ of $0$ in $K$ such that $\Phi(gk) = \Phi(g)$ whenever all entries of $k - 1$ lie in $U$, and
$$\Phi\big(n(z)\, m(s)\, g\big) = \eta_K(s)\, |s|_K\, \Phi(g) \quad \text{for all } z \in K,\ s \in K^\times,\ g \in \mathrm{SL}_2(K).$$

These are the smooth vectors of the representation of $\mathrm{SL}_2(K)$ induced from the character $n(z)m(s) \mapsto \eta_K(s)|s|_K$ of the Borel subgroup, in the sense of [smooth representations](/learn/representations/#smooth-representations-of-p-adic-groups).

**Definition 4.3.5 (Truncated Whittaker integral).** Let $\mathcal{O}_K$ be the set of $z \in K$ whose characteristic polynomial over $F$ has coefficients of norm at most $1$, that is, the integral elements of $K$. For an induced $\Phi$, $a \in K$ and $c \in F$ put
$$W_c(a, \Phi) = \int_{\{z \,:\, cz \in \mathcal{O}_K\}} \Phi\big(w\, n(z)\big)\, \psi_K(-a z)\, d\mu_K(z).$$

As $c \to 0$ the domain grows to all of $K$, and $W_c(a, \Phi)$ approximates the Whittaker functional at $a$.

Two kinds of induced functions occur. The first comes from a Weil representation: for a test function $\varphi$ on $L$, put $j_\varphi(g) = W(g)\varphi(0)$. The second comes from the linear side. For a test function $\varphi'$ on $K \times K$, let $\tilde\varphi'(c, u) = \int_K \varphi'(b, c)\, \psi_K(ub)\, d\mu_K(b)$, and put
$$J_{\varphi'}(g) = \int_K \tilde\varphi'\big(t g_{21},\, t g_{22}\big)\, \eta_K(t)\, d\mu_K(t),$$
where $g_{21}, g_{22}$ are the entries of the second row of $g$. Let $\mathcal{F}_K \varphi'(p_1, p_2) = \int_K \int_K \varphi'(b', c')\, \psi_K(p_1 c' + b' p_2)\, dc'\, db'$ be the Fourier transform on $K \times K$.

**Lemma 4.3.6 (Induced functions).** Let $\mu_K$ be self-dual for $\psi_K(yy')$.

1. Let $W$ be a Weil representation with data $x \in K^\times$, $\eta_K$, $\mu$, $\gamma$, and $\varphi$ a test function. Then $j_\varphi$ is induced, and $\gamma \neq 0$ if $\varphi \neq 0$.
2. For a test function $\varphi'$, $J_{\varphi'}$ is induced, and $J_{\mathcal{F}_K\varphi'}(h) = J_{\varphi'}(hw)$ for all $h$.

Lean: `GlobalTheory.T.weilRep_evalZero_mem_induced`, `GlobalTheory.T.jHyp_mem_induced_fourier_weyl`.

*Proof.* We show the parts of item 1 that follow from the formulas. For $g \in \mathrm{SL}_2(K)$,
$$j_\varphi(n(z)m(s)g) = \psi_K\big(z x N(0)\big)\, \eta_K(s)\, |s|_K\, \big(W(g)\varphi\big)(s \cdot 0) = \eta_K(s)\,|s|_K\, j_\varphi(g).$$
If $\gamma = 0$, then $W(w)$ kills every test function, so $\eta_K(-1)\varphi(-y) = W(m(-1))\varphi(y) = W(w)W(w)\varphi(y) = 0$, and $\varphi = 0$. The smoothness of $j_\varphi$, and item 2, which is Fourier inversion on $K$, are proved apart and not reproduced here. $\square$

**Lemma 4.3.7 (Limits of Whittaker integrals).** Let $\mu_K, \mu_{L,x}, \nu$ be rank one measures and $a$ a unit of $K$.

1. Let $x \in K^\times$, let $W$ be a Weil representation with data $x$, $\eta_K$, $\mu_{L,x}$, $\gamma$, and $\varphi$ a test function on $L$. If $a = x N(y)$ for a unit $y$, then $W_c(a, j_\varphi) = \gamma\, O_L(\varphi, y)$ for all $c \neq 0$ near $0$. If $a$ is not of this form, then $W_c(a, j_\varphi) = 0$ for all $c \neq 0$ near $0$.
2. For a test function $\varphi'$ on $K \times K$, $W_c(a, J_{\varphi'}) = O_K(\varphi', a)$ for all $c \neq 0$ near $0$.

Lean: `GlobalTheory.T.truncatedWhittaker_weilRep_eventually`, `GlobalTheory.T.truncatedWhittaker_jHyp_eq_orbitalIntegral`.

*Proof.* We give the main step of item 1. Since $B_x(y, 0) = 1$,
$$j_\varphi(w\,n(z)) = \gamma \int_L \varphi(y)\, \psi_K\big(z x N(y)\big)\, d\mu_{L,x}(y).$$
Put this in $W_c(a, j_\varphi)$ and integrate over $z$ first. The inner integral of $\psi_K(z(xN(y) - a))$ over $c^{-1}\mathcal{O}_K$ is a multiple of the indicator function of a shrinking neighbourhood of the fibre $xN(y) = a$. The integration formula for $N$ turns the limit into $\gamma\, O_L(\varphi, y)$, and into $0$ when the fibre is empty. Since $\varphi$ is locally constant with compact support, the expression is constant for small $c$. Item 2 is the same computation on $K \times K$. $\square$

**Lemma 4.3.8 (Kirillov vanishing).** Let $\mu_K$ be self-dual for $\psi_K(yy')$. Let $\Psi$ be induced, and assume $W_c(a, \Psi) \to 0$ as $c \to 0$, $c \neq 0$, for every unit $a$ of $K$. Then $\Psi(w\,n(z)) = 0$ for every $z \in K$, and $W_c(a, \Psi(\cdot\, w)) = 0$ for every $a \in K$ and $c \in F$.

Lean: `GlobalTheory.T.kirillov_vanishing_of_limit`.

The name refers to the Kirillov model of the induced representation, in which a vector is described by its Whittaker functionals. The proof is not reproduced here.

**Theorem 4.3.9 (Rank one transfer).** Let $\mu_K, \mu_{L,x}, \nu$ be rank one measures and $S$ a set of representatives. For each $x \in S$ let $W_x$ be a Weil representation with data $x$, $\eta_K$, $\mu_{L,x}$, $\gamma_x$. Let $\varphi'$ be a test function on $K \times K$, let $\varphi_x$ be a test function on $L$ for each $x \in S$, and let $\kappa \in \mathbb{C}$. Assume
$$\kappa\, O_K\big(\varphi', x N(y)\big) = O_L(\varphi_x, y) \quad \text{for all } x \in S \text{ and } y \in L^\times.$$
Then for all $x \in S$ and $y \in L^\times$,
$$\kappa\, O_K\big(\mathcal{F}_K\varphi', x N(y)\big) = \gamma_x\, O_L\big(\mathcal{F}_{B_x}\varphi_x, y\big),$$
where $\mathcal{F}_{B_x}$ is the Fourier transform for $\mu_{L,x}$.

Lean: `GlobalTheory.JR.RankOneTransfer.rankOne` (also `GlobalTheory.T.etaleOrbitalFourier_rankOne_transfer`, a second name).

*Proof.* The set $S$ is finite. If $x_0 N(y_0) = x_1 N(y_1)$ with $x_0, x_1 \in S$, then $x_0 = x_1$ by uniqueness. For $x' \in S$ let $r_{x'} = -\gamma_{x'}^{-1}$ if $\gamma_{x'} \neq 0$ and $r_{x'} = 0$ otherwise, and put
$$\Psi = \sum_{x' \in S} r_{x'}\, j_{\varphi_{x'}} + \kappa\, J_{\varphi'},$$
where $j_{\varphi_{x'}}$ is formed with $W_{x'}$. By the Lemma on induced functions, $\Psi$ is induced.

Step 1: the Whittaker integrals of $\Psi$ vanish in the limit. Let $a$ be a unit and write $a = x_0 N(y_0)$ with $x_0 \in S$. For $c \neq 0$, $W_c(a, \cdot)$ is linear. By the Lemma on limits, for $c \neq 0$ near $0$,
$$W_c(a, \Psi) = r_{x_0}\gamma_{x_0}\, O_L(\varphi_{x_0}, y_0) + \kappa\, O_K(\varphi', a),$$
since the terms with $x' \neq x_0$ vanish. If $\gamma_{x_0} \neq 0$, this is $-O_L(\varphi_{x_0}, y_0) + \kappa O_K(\varphi', x_0 N(y_0)) = 0$ by the hypothesis. If $\gamma_{x_0} = 0$, then $\varphi_{x_0} = 0$ by the Lemma on induced functions, so the hypothesis gives $\kappa O_K(\varphi', a) = 0$ and again $W_c(a, \Psi) = 0$.

Step 2: Kirillov vanishing gives $W_c(a, \Psi(\cdot\, w)) = 0$ for all $a$ and $c$.

Step 3: compute $\Psi(\cdot\, w)$. Since $W_{x'}$ is a representation, $j_{\varphi_{x'}}(hw) = j_{\varphi^w_{x'}}(h)$ with $\varphi^w_{x'} = W_{x'}(w)\varphi_{x'}$, a test function. By the Lemma on induced functions, $J_{\varphi'}(hw) = J_{\mathcal{F}_K\varphi'}(h)$. So
$$\Psi(\cdot\, w) = \sum_{x' \in S} r_{x'}\, j_{\varphi^w_{x'}} + \kappa\, J_{\mathcal{F}_K\varphi'}.$$
Fix $x \in S$ and $y \in L^\times$, and put $a = x N(y)$. Apply the Lemma on limits to this sum, as in Step 1, and use Step 2:
$$0 = r_x \gamma_x\, O_L(\varphi^w_x, y) + \kappa\, O_K(\mathcal{F}_K\varphi', a).$$
Since $\varphi^w_x = \gamma_x \mathcal{F}_{B_x}\varphi_x$, we get $O_L(\varphi^w_x, y) = \gamma_x O_L(\mathcal{F}_{B_x}\varphi_x, y)$. If $\gamma_x \neq 0$, then $r_x\gamma_x = -1$ and the claim follows. If $\gamma_x = 0$, then $r_x = 0$, so $\kappa O_K(\mathcal{F}_K\varphi', a) = 0$, which is the claim. $\square$

**Remark 4.3.10 (Formalization).** The three lemmas of this section are proved in their own files, which this chapter does not cover; the proofs above give only their main steps. In the theorem, $\gamma_x^{-1}$ is the inverse in $\mathbb{C}$ with $0^{-1} = 0$, which is the convention used for $r_x$ above. The theorem asks for no relation between the measures $\mu_{L,x}$ for different $x$.
