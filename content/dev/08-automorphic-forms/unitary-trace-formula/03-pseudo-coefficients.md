---
title: Pseudo-coefficients
decls:
  - GlobalTheory.PsCo.Pc.localPC_holds
  - GlobalTheory.T.localPseudoCoefficientExistence_unitaryGroup
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Pseudo-coefficients

This section proves that a discrete series representation $D$ of $G_\varepsilon = \mathrm{U}(p, q)$, with $p + q$ odd and a parameter whose gaps are large, has a pseudo-coefficient: a smooth compactly supported function $f$ whose trace is $1$ on $D$ and $0$ on every other unitary irreducible representation, and whose orbital integrals are known at every regular semisimple element. The proof puts together [the data on $K$](/entry/st-kdata-of/) and [the Koszul family](/entry/st-alg/) with [its limits](/entry/st-lim/). The theorem is the archimedean input of the simple trace formula for unitary groups: it is used in [the comparison of cuspidal multiplicities](/entry/mult-eq-of-sides/) of this chapter and in [the Harish-Chandra and Langlands step](/entry/unitary-theory-of-harish-chandra-langlands-alt/) of Volume 14. For the background, see [the simple trace formula and pseudo-coefficients](/learn/trace-formula/#arthurs-trace-formula-the-simple-trace-formula-and-pseudo-coefficients) and [discrete series](/learn/representations/#discrete-series).

We keep the notation of the two previous sections. An element $s \in G_\varepsilon$ is *regular semisimple* if its characteristic polynomial is separable. Its centralizer $G_s$ is then a torus. For a Haar measure $\mu$ on $G_\varepsilon$ and a Haar measure $dt$ on $G_s$, the *orbital integral* of $f$ at $s$ is
$$O_s(f) = \int_{G_s \backslash G_\varepsilon} f(x^{-1} s x)\, \frac{d\mu(x)}{dt}.$$
For a unitary representation $\pi$ of $G_\varepsilon$ on a Hilbert space, let $\pi(f) = \int_{G_\varepsilon} f(g)\, \pi(g)\, d\mu(g)$.

**Definition 2.3.1 (Pseudo-coefficient).** Let $D$ be a discrete series of $G_\varepsilon$ with parameter $\lambda$, and $\mu$ a Haar measure. A function $f : G_\varepsilon \to \mathbb{C}$ is a *pseudo-coefficient of $D$ with known orbital integrals* if:

1. $f$ is smooth with compact support, as a function of the matrix entries;
2. $f$ is bi-$K_\varepsilon$-finite: its translates $g \mapsto f(k g k')$, $k, k' \in K_\varepsilon$, span a finite-dimensional space;
3. $D(f)$ is trace class with trace $1$;
4. for every unitary irreducible $\pi$ that is not unitarily equivalent to $D$, $\pi(f)$ is trace class with trace $0$;
5. for every regular semisimple $s$ with noncompact centralizer and every Haar measure on $G_s$, $O_s(f) = 0$;
6. for every regular semisimple $s$ with compact centralizer, every $y$ and $\theta$ with $y^{-1} s y = t_\theta$, and every Haar measure $dt$ on $G_s$,
$$O_s(f) = \frac{\overline{\Theta_\lambda(t_\theta)}}{\mathrm{vol}(G_s, dt)}.$$

Conditions 3 and 4 are the defining property of a pseudo-coefficient in the sense of Clozel and Delorme. Conditions 5 and 6 give its orbital integrals: they vanish off the elliptic set, and on the elliptic set they are given by the conjugate of the discrete series character. This is the form in which the elliptic terms of the trace formula are computed in [the elliptic side](/entry/elliptic-side-direct/).

**Theorem 2.3.2 (Pseudo-coefficients for $\mathrm{U}(p, q)$).** Let $r$ be odd, $\varepsilon \in \{\pm 1\}^r$, and $\lambda \in \mathbb{Z}^r$ with $\lambda_i - \lambda_{i+1} \ge 100\, r^4$ for $1 \le i < r$. Let $D$ be a discrete series of $G_\varepsilon$ with parameter $\lambda$, and $\mu$ a Haar measure on $G_\varepsilon$. Then $D$ has a pseudo-coefficient with known orbital integrals.

Lean: `GlobalTheory.PsCo.Pc.localPC_holds` (also `GlobalTheory.T.localPseudoCoefficientExistence_unitaryGroup`, a second name).

The proof uses the following facts about the functions of [the previous section](/entry/st-lim/).

* *Shapes.* For $d \ge 0$ let $\mathcal{S}_d$ be the span of the functions $g \mapsto H(\rho(g))\, P(g)$ with $H$ smooth and zero on $[R, \infty)$ for some $R$, and $P$ of degree at most $d$. Every element of $\mathcal{S}_d$ is smooth, compactly supported and bi-$K_\varepsilon$-finite.
* *Lie derivatives.* Let $\mathcal{A}$ be the span of the functions $D_Z(H(\rho) P)$ with $Z$ in the Lie algebra of $G_\varepsilon$ and $H$, $P$ as above. Every element of $\mathcal{A}$ has orbital integral $0$ at every regular semisimple element, and its operator has trace $0$ in every unitary irreducible representation.
* *The family.* For a profile $G$ of order $N$ and polynomials $p_k$ there is $d$ with $\varphi_t \in \mathcal{S}_d$ for all $t > 0$. If $(p_k, q_{x, k})$ are Koszul data, then $\varphi_1 - \varphi_t \in \mathcal{A}$ for every $t \ge 1$. Profiles of every order exist.
* *Traces.* For a unitary irreducible $\pi$ and $d \ge 0$ there is a continuous function $w_\pi$ on $G_\varepsilon$ such that $\mathrm{tr}\, \pi(\varphi) = \int_{G_\varepsilon} \varphi\, w_\pi\, d\mu$ for all $\varphi \in \mathcal{S}_d$, and such that for every polynomial $P$ of degree at most $d$ the operator $\int_{K_\varepsilon} P(k)\, \pi(k)\, dk$ has trace $\int_{K_\varepsilon} P\, w_\pi\, dk$.
* *Geometry.* If $s$ is regular semisimple with noncompact centralizer, there is $R > 0$ with $\rho(x^{-1} s x) \ge R$ for all $x$. If the centralizer is compact, then for every continuous compactly supported $f$ and every $y$, $O_s(f) = \mathrm{vol}(G_s)^{-1} \int_{G_\varepsilon} f(x^{-1} y^{-1} s y x)\, d\mu(x)$.

The function $w_\pi$ is the character of $\pi$ restricted to the shapes of bounded degree; for the existence of the character as a locally integrable function, see [discrete series](/learn/representations/#discrete-series).

*Proof.* Let $M$ and $P$ be the data of [the Theorem on $K$](/entry/st-kdata-of/), and $\Phi = \Phi_M(P)$. By [the algebraic step](/entry/st-alg/) there are Koszul data with $p_N = \Phi$. Choose a profile $G$ of order $N$, and let $c \ne 0$ be the constant of [the limits](/entry/st-lim/). Put $\varphi_t = c^{-1} \sum_k t^k G^{(k)}(t \rho)\, p_k$ and $f = \varphi_1$. By the facts on the family, $\varphi_t \in \mathcal{S}_d$ for some $d$ and all $t \ge 1$, and $\varphi_1 - \varphi_t \in \mathcal{A}$. So $f$ is smooth, compactly supported and bi-$K_\varepsilon$-finite.

*Traces.* Let $\pi$ be unitary irreducible, and $w_\pi$ as above. Since $\varphi_1 - \varphi_t$ has trace $0$ in $\pi$, the number $\int \varphi_t\, w_\pi\, d\mu$ does not depend on $t \ge 1$. By the first limit it tends to $\int_K \Phi\, w_\pi\, dk$, which is the trace of $B_\pi = \int_K \Phi(k)\, \pi(k)\, dk$. So $\pi(f)$ and $B_\pi$ are both trace class with the same trace. For $\pi = D$ this trace is $1$, and for $\pi$ not equivalent to $D$ it is $0$, by properties 3 and 4 of $\Phi$.

*Noncompact centralizer.* Let $R > 0$ with $\rho(x^{-1} s x) \ge R$ for all $x$, and put $t = 1 + 2/R$. Then $t \rho(x^{-1} s x) \ge R + 2 > 1$, so $\varphi_t$ vanishes on the conjugacy class of $s$ and $O_s(\varphi_t) = 0$. Since $f = \varphi_t + (\varphi_1 - \varphi_t)$ and the second term is in $\mathcal{A}$, $O_s(f) = 0$.

*Compact centralizer.* Let $y^{-1} s y = t_\theta$. The characteristic polynomial of $t_\theta$ is separable, so the $e^{i\theta_a}$ are distinct. By the geometric fact, $O_s(\varphi_t) = \mathrm{vol}(G_s)^{-1} \int \varphi_t(x^{-1} t_\theta x)\, d\mu(x)$, and as before this does not depend on $t \ge 1$. Since $\Phi$ is a class function on $K_\varepsilon$, the second limit applies:
$$O_s(f) = \frac{c^{-1}\, c\, \Phi(t_\theta)}{d_\varepsilon(\theta)\, \mathrm{vol}(G_s)} = \frac{\overline{\Theta_\lambda(t_\theta)}}{\mathrm{vol}(G_s)},$$
by property 2 of $\Phi$; here $d_\varepsilon(\theta) \ne 0$ because the $e^{i\theta_a}$ are distinct. $\square$

The classical existence theorem is stated for every discrete series of a real reductive group, with no gap condition and no parity condition; see the notes at the end of the chapter. The gap condition here comes from the method: the trace of $B_\pi$ is controlled by the lowest $K$-type through a supertrace, and the proof of that step needs the parameter far from the walls.

**Remark 2.3.3 (Formalization).** The proof is a composition of twelve named inputs: the two Propositions of [the previous section](/entry/st-lim/), the Theorem on $K$, and the facts listed above ([LocalPseudoCoefficientExistenceUnitaryGroup.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalPseudoCoefficientExistenceUnitaryGroup.lean#L21), [EqOfConstOfTendsto.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EqOfConstOfTendsto.lean#L47)). The second name is a restatement by `first | exact …`. The intermediate statement of the proof repeats the conclusion with a second copy of the gap condition ([EqOfConstOfTendsto.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EqOfConstOfTendsto.lean#L15)). Condition 4 is asked for every unitary irreducible representation, not only for the tempered ones. A representation is a homomorphism from $G_\varepsilon$ to bounded operators, with unitarity and topological irreducibility as separate conditions; we did not unfold the definition of the discrete series with parameter $\lambda$, or that of the character $\Theta_\lambda$, which is used only through property 2 of $\Phi$.
