---
title: The inverse and swap reductions for unitary groups
decls:
  - GlobalTheory.T.unitary_inverse_reduction
  - GlobalTheory.CompanionTheory.InvStep.invStepU
  - GlobalTheory.T.unitary_swap_reduction
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The inverse and swap reductions for unitary groups

An irreducible unramified representation of a quasi-split unitary group embeds into many principal series, one for each Weyl conjugate of its parameters. The embedding theorem [Theorem 7.7 of Volume 8](/entry/extreme-u/) picks one whose parameters are in a fixed order, and it gets there by two kinds of moves: swap two neighbouring parameters, or invert the last one. This section states both moves and proves the second. The tool is an intertwining integral over a one-root unipotent group, whose value on the spherical vector is a rank one factor of Gindikin-Karpelevich type. The proof of the swap move is in [Theorem 1.11.6](/entry/swap-step-u/). For background see [smooth representations of p-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups) and [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module).

### Setting

Let $L$ be a complete field with a discrete valuation, normalized so that a fixed element $\varpi$ has order $1$. Let $\sigma$ be a field automorphism of $L$ with $\sigma^2 = 1$ that preserves the valuation and fixes $\varpi$, and suppose some integral $x$ has $\sigma x - x$ a unit. Let the residue field of $L$ have $q^2$ elements, with $q \geq 2$. We call these assumptions unramified. Let $J$ be the antidiagonal $n \times n$ matrix with entries $1$, let $G$ be the unitary group of $J$ relative to $\sigma$ inside $\mathrm{GL}_n(L)$, and let $K$ be its subgroup of integral matrices. Let $B$ be the upper triangular elements of $G$ and $N$ the upper unipotent ones. Put $m = \lfloor n/2 \rfloor$.

For $\alpha = (\alpha_1, \dots, \alpha_m) \in (\mathbb{C}^\times)^m$ and $b \in B$ put
$$\chi_\alpha(b) = \prod_{i=1}^{m} \alpha_i^{\mathrm{ord}(b_{ii})}\, q^{-(n+1-2i)\,\mathrm{ord}(b_{ii})}.$$
Let $I(\alpha)$ be the space of functions $\varphi \colon G \to \mathbb{C}$ with $\varphi(bg) = \chi_\alpha(b)\varphi(g)$ for $b \in B$, $g \in G$, with $G$ acting by right translation. A representation $\rho$ of $G$ on $V$ is spherical when $V^K \neq 0$, and smooth when every $v$ has an open stabilizer.

### The two moves

**Theorem 1.10.1 (Swap reduction).** Assume the unramified setting. Let $\rho$ be an irreducible admissible spherical representation of $G$ on $V$, let $\alpha \in (\mathbb{C}^\times)^m$, and let $1 \leq i < m$ with $|\alpha_i/\alpha_{i+1}| < 1$. If $f \colon V \to I(\alpha)$ is an injective $G$-map, there is an injective $G$-map $V \to I(\alpha')$, where $\alpha'$ is $\alpha$ with $\alpha_i$ and $\alpha_{i+1}$ exchanged.

Lean: `GlobalTheory.T.unitary_swap_reduction`.

**Theorem 1.10.2 (Inverse reduction).** Assume the unramified setting, $m \geq 1$. Let $\rho$ be an irreducible admissible spherical representation of $G$ on $V$, and let $\alpha \in (\mathbb{C}^\times)^m$ with $|\alpha_m| < 1$. If $f \colon V \to I(\alpha)$ is an injective $G$-map, there is an injective $G$-map $V \to I(\alpha')$, where $\alpha' = (\alpha_1, \dots, \alpha_{m-1}, \alpha_m^{-1})$.

Lean: `GlobalTheory.CompanionTheory.InvStep.invStepU` (also `GlobalTheory.T.unitary_inverse_reduction`, the same statement).

### The cell

Let $s$ be the permutation of $\{1, \dots, n\}$ that exchanges $m$ and $n + 1 - m$. For $n$ even these are the two middle positions, and for $n$ odd they surround the middle one. Let $y \in K$ be a monomial matrix with pattern $s$, that is $y_{ij} = 0$ unless $i = s(j)$. Let $N_y$ be the group of $u \in N$ with $y^{-1}uy$ lower triangular, and $\mu$ the Haar measure on $N_y$ with $\mu(N_y \cap K) = 1$. Put
$$c(z) = \frac{1 - q^{-1}z}{1 - z} \ (n \text{ even}), \qquad c(z) = \frac{(1 - q^{-2}z)(1 + q^{-1}z)}{1 - z^2} \ (n \text{ odd}).$$

We take the following facts as given; they are proved elsewhere in the development.

**Theorem 1.10.3 (Inputs).** Assume the unramified setting.

- (i) $K$ is open and compact, $G = BK$, and every $b \in B$ is $t\nu$ with $t$ diagonal and $\nu \in N$. Such $y$ and $\mu$ exist.
- (ii) For each $\alpha$ there is $\Phi_\alpha \in I(\alpha)$, right invariant under $K$, with $\Phi_\alpha(1) = 1$. Every right $K$-invariant $\psi \in I(\alpha)$ equals $\psi(1)\Phi_\alpha$.
- (iii) Let $n$ be even and $H_j$, for $j \geq 0$, the set of $u \in N_y$ with $\mathrm{ord}(u_{m, n+1-m}) \geq -j$. Then $\mu(H_j) = q^j$, and $\Phi_\alpha(y^{-1}u)$ equals $1$ on $H_0$ and $(\alpha_m/q)^{j+1}$ on $H_{j+1} \setminus H_j$. If $|z| < 1$, a function with these values has integral $c(z)$ at $z = \alpha_m$.
- (iv) Let $n$ be odd and $|\alpha_m| < 1$. Then $u \mapsto \Phi_\alpha(y^{-1}u)$ is integrable on $N_y$ with integral $c(\alpha_m)$.
- (v) For diagonal $t \in G$ there is $s_t \in \mathbb{C}$ with $\int_{N_y} F(t^{-1}ut)\,d\mu(u) = s_t\int_{N_y} F\,d\mu$ for all $F$, and $\chi_\alpha(y^{-1}ty)\,s_t = \chi_{\alpha'}(t)$.
- (vi) If $\psi(bg) = \chi_\alpha(b)\psi(g)$ for all $b \in B$, then for $\nu \in N$, $\int_{N_y}\psi(y^{-1}u\nu)\,d\mu(u) = \int_{N_y}\psi(y^{-1}u)\,d\mu(u)$.

In (v), $y^{-1}ty$ is again diagonal, so $\chi_\alpha$ is defined on it. Fact (vi) comes from a change of variables in $N_y$: on the left for $n$ even, and on the right, with right invariance of $\mu$, for $n$ odd.

**Lemma 1.10.4 (The spherical function on the cell).** If $|\alpha_m| < 1$, then $u \mapsto \Phi_\alpha(y^{-1}u)$ is integrable on $N_y$ and $\int_{N_y}\Phi_\alpha(y^{-1}u)\,d\mu(u) = c(\alpha_m)$. Also $c(\alpha_m) \neq 0$.

*Proof.* For $n$ odd this is (iv). For $n$ even the sets $H_j$ increase and cover $N_y$, since every entry has a finite order or is $0$. With $z = \alpha_m$ the integral is
$$1 + \sum_{j \geq 0}(q^{j+1} - q^j)\Big(\frac{z}{q}\Big)^{j+1} = 1 + (1 - q^{-1})\frac{z}{1 - z} = \frac{1 - q^{-1}z}{1 - z},$$
and (iii) gives integrability and this value. For the last claim, $|q^{-1}z|$, $|q^{-2}z|$ and $|z^2|$ are less than $1$, so none of $1 - q^{-1}z$, $1 - q^{-2}z$, $1 + q^{-1}z$, $1 - z$, $1 - z^2$ vanishes. $\square$

**Lemma 1.10.5 (Integrability).** Let $|\alpha_m| < 1$, and let $\psi \in I(\alpha)$ be right invariant under an open set $S \ni 1$, in the sense that $\psi(xg) = \psi(x)$ for $g \in S$ and all $x$. Then $u \mapsto \psi(y^{-1}u)$ is integrable on $N_y$.

*Proof.* Near any $g$, the points $x \in gS$ satisfy $\psi(x) = \psi(g)$, so $\psi$ is locally constant, hence continuous. As $K$ is compact, $|\psi| \leq C$ on $K$ for some $C \geq 0$. For $g = b\kappa$ with $b \in B$, $\kappa \in K$, $|\psi(g)| = |\chi_\alpha(b)||\psi(\kappa)| \leq C|\chi_\alpha(b)| = C|\Phi_\alpha(g)|$. So $|\psi(y^{-1}u)| \leq C|\Phi_\alpha(y^{-1}u)|$, which is integrable by the previous lemma. $\square$

**Lemma 1.10.6 (Transformation law).** Let $\psi$ satisfy $\psi(bg) = \chi_\alpha(b)\psi(g)$ for $b \in B$. Then for $b \in B$,
$$\int_{N_y}\psi(y^{-1}ub)\,d\mu(u) = \chi_{\alpha'}(b)\int_{N_y}\psi(y^{-1}u)\,d\mu(u).$$

*Proof.* Write $b = t\nu$ as in (i). Then $y^{-1}ut\nu = (y^{-1}ty)\,y^{-1}(t^{-1}ut)\nu$, and $y^{-1}ty \in B$, so $\psi(y^{-1}ut\nu) = \chi_\alpha(y^{-1}ty)\,\psi(y^{-1}(t^{-1}ut)\nu)$. Integrate. By (v) applied to $F(x) = \psi(y^{-1}x\nu)$, and then (vi), the integral is $\chi_\alpha(y^{-1}ty)\,s_t\int\psi(y^{-1}u)\,d\mu = \chi_{\alpha'}(t)\int\psi(y^{-1}u)\,d\mu$. Finally $\chi_{\alpha'}(t) = \chi_{\alpha'}(t\nu)$, since $\chi_{\alpha'}$ only sees the diagonal. $\square$

### Proof of the inverse reduction

*Proof of the inverse reduction.* For $v \in V$ write $f_v = f(v)$. Since $f$ is a $G$-map, $f_{\rho(g)v}(x) = f_v(xg)$. Put
$$\lambda(v) = \int_{N_y} f_v(y^{-1}u)\,d\mu(u).$$
Since $\rho$ is smooth, $S = \{g : \rho(g)v = v\}$ is open, and $f_v(xg) = f_{\rho(g)v}(x) = f_v(x)$ for $g \in S$. By the lemma on integrability the integral converges, so $\lambda$ is linear. By the transformation law, $\lambda(\rho(b)v) = \int f_v(y^{-1}ub)\,d\mu = \chi_{\alpha'}(b)\lambda(v)$ for $b \in B$.

Define $F(v)(g) = \lambda(\rho(g)v)$. Then $F(v)(bg) = \lambda(\rho(b)\rho(g)v) = \chi_{\alpha'}(b)F(v)(g)$, so $F(v) \in I(\alpha')$, and $F(\rho(g)v)(x) = F(v)(xg)$, so $F$ is a $G$-map.

Let $v_0 \neq 0$ be fixed by $K$. Then $f_{v_0}$ is right $K$-invariant and lies in $I(\alpha)$, so $f_{v_0} = f_{v_0}(1)\Phi_\alpha$ by (ii). If $f_{v_0}(1) = 0$, then $f_{v_0} = 0$, against the injectivity of $f$. By the lemma on the spherical function,
$$F(v_0)(1) = \lambda(v_0) = f_{v_0}(1)\,c(\alpha_m) \neq 0.$$
The kernel of $F$ is a subrepresentation of $V$ that does not contain $v_0$. Since $\rho$ is irreducible, it is zero. So $F$ is injective. $\square$

The swap reduction has the same shape. There the integral runs over a one-parameter root group $x \mapsto u(x)$ for the pair $(i, i+1)$. The function $x \mapsto f_v(s\,u(x)\,g)$ belongs to a class of functions on $L$ on which a translation-invariant functional with a known scaling law is defined. The condition $|\alpha_i/\alpha_{i+1}| < 1$ is what makes that functional exist, and its value on the spherical vector is again a nonzero rank one factor.

**Remark 1.10.7 (Formalization).** The inverse reduction is `invStepU` in [UnitaryInverseReduction.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitaryInverseReduction.lean#L238), and the wrapper is in [UnitaryInverseReductionStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitaryInverseReductionStatement.lean#L7). The statements `InvStepU` and `SwapStepU` are in [SatPowNonvan.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/StrictDominance/UnitaryExtremality/SatPowNonvan.lean#L81), `SwapStepU` at L81 and `InvStepU` at L90. The swap wrapper, in [UnitarySwapReductionStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitarySwapReductionStatement.lean#L7), applies `swapStepU` from [UnitarySwapReduction.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitarySwapReduction.lean#L136). Both statement files import Mathlib twice. The lemmas of this section are `spherical_cell` (L94, with the even case `spherical_even` at L28), `cSimpleU_ne_zero` (L110), `integrable_cell` (L206) and `integral_law` (L183), built from `scale_cell` (L143) and `shift_cell` (L163). Our $I(\alpha)$ is `psSpaceU`. It has no smoothness condition: it holds every function with the transformation law. Our $N_y$ is `cellU y`, the indices are from $0$ in Lean, and the last index is given by `j.val + 1 = n / 2`. Of `IsAdmissible ρ` the proofs use only the first half, smoothness, via `hadm.1`. The finiteness of fixed vectors is never used. The value $c$ is `cSimpleU`, built from `cSL` and `cSU`. The input (iii) is assembled in `spherical_even` from a shell measure lemma and a geometric series lemma.
