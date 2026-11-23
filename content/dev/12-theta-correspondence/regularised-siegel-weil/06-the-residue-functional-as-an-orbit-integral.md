---
title: The residue functional as an orbit integral
decls:
  - PositivityTheory.Rg.Rsw.Cell.muCell
  - PositivityTheory.Rg.Rsw.Em.eisMeas
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The residue functional as an orbit integral

At the edge $s = p/2$ the Siegel Eisenstein series on $G_p$ has at most a simple pole, by the bound of the first section. Its residue is a linear functional on sections, and it is positive. This section writes that functional as an integral in two steps. First, on sections of a fixed level, the residue is a nonnegative multiple of the integral over the big cell. Second, for the reduced section of a Siegel-Weil section, the residue is an integral against an orbit measure of the last section. The second result, with the theta-side measure of the last section, is the input of the proof of [Theorem 5.7.3](/entry/res-core/), where the two measures are compared.

We keep the notation of the earlier sections. Recall from the second section that $f$ is a section of degree $s$ for $\chi$ if $f(qg) = \chi(\det a_q)\, |\det a_q|^{s + p/2} f(g)$ for $q \in P_p$. Write $\mathcal{R}_p$ for the space of continuous sections of degree $p/2$ for the trivial character, and $E(f)$ for the Eisenstein sum of the first section.

**Definition 5.6.1 (Residue functional).** A *residue functional* on $G_p$ is a map $\mu$ from functions on $G_p$ to $\mathbb{C}$ such that:

1. $\mu$ is additive and $\mathbb{C}$-homogeneous on $\mathcal{R}_p$;
2. if $f \in \mathcal{R}_p$ takes values in $[0, \infty)$, then $\mu(f)$ is real and $\mu(f) \ge 0$;
3. for each height $H$ on $G_p$ there is $C$ with $|\mu(f)| \le C B$ for all $f \in \mathcal{R}_p$ and $B \in \mathbb{R}$ with $|f| \le B H^p$;
4. $\mu(f) = \mu(f(\cdot\, x))$ for $f \in \mathcal{R}_p$ and $x$ upper unipotent or in $G_p(F)$;
5. if $(\sigma, g) \mapsto f_\sigma(g)$ is continuous on $[p/2, p/2 + 1] \times G_p$, each $f_\sigma$ is a section of degree $\sigma$ for the trivial character, and $(\sigma - p/2)\, E(f_\sigma)(1) \to a$ as $\sigma \to p/2$ from above, then $a = \mu(f_{p/2})$.

Property 5 says that $\mu$ is the residue of the [Eisenstein series](/learn/automorphic-forms/#eisenstein-series) at the edge, and property 2 says that this residue is positive. Properties 3 and 4 are what the residue inherits from the bound at the edge and from the invariance of the Eisenstein series.

### The cell formula

For an $S$-idempotent $e$ (fifth section) let $\mathrm{Herm}_p^S(e)$ be the group of $x \in \mathrm{Herm}_p(\mathbb{A}_E)$ with $ex = x$, and let $n(x) = \begin{pmatrix} 1 & x \\ 0 & 1 \end{pmatrix}$. So $\mathrm{Herm}_p^S(e)$ is the part of the Hermitian matrices that lives at the archimedean places and at $S$. Recall the level subgroup $K^S$ of the fourth section.

**Theorem 5.6.2 (Cell formula).** Assume the conclusions of the existence of heights and of the theorem on idempotents. Let $\mu$ be a residue functional on $G_p$ and $w$ a Weyl element. Then there is a finite set $S_0$ of finite places such that for each finite $S \supseteq S_0$, each $S$-idempotent $e$ and each Haar measure $\lambda$ on $\mathrm{Herm}_p^S(e)$, one of the following holds:

1. $\mu(f) = 0$ for all $f \in \mathcal{R}_p$ that are right invariant under $K^S$;
2. there is $c > 0$ such that for all $f \in \mathcal{R}_p$ that are right invariant under $K^S$, the function $x \mapsto f(w\, n(x))$ is $\lambda$-integrable and
$$\mu(f) = c \int_{\mathrm{Herm}_p^S(e)} f(w\, n(x))\, d\lambda(x).$$

Lean: `PositivityTheory.Rg.Rsw.Cell.muCell`.

*Proof.* We give the route; each step is a lemma that we take as given. From the existence of heights one gets a positive $h \in \mathcal{R}_p$ that is right invariant under $K^S$ and invariant under right translation by $n(y)$ and by $w\, n(y) w^{-1}$. Dividing by $h$ turns elements of $\mathcal{R}_p$ into functions on $P_p \backslash G_p$. The positivity of $\mu$ and the Riesz representation theorem give a measure $\nu$ on $P_p \backslash G_p$ with $\mu(f) = \int (f/h)\, d\nu$. Let the *cell* of $e$ be the open set of $g \in G_p$ such that $\det((1 - e) + e\, c_g)$ is a unit, where $c_g$ is the lower left block of $g$. The complement of the cell is $\nu$-null, by the invariance of $\mu$ and a bound on the size of the complement. Each $g$ in the cell is $q\, w\, n(\tau(g))\, u$ with $q \in P_p$, $\tau(g) \in \mathrm{Herm}_p^S(e)$ and $u \in K^S$, where $u$ commutes with $n(x)$ for $x \in \mathrm{Herm}_p^S(e)$. So on the cell a $K^S$-invariant $f \in \mathcal{R}_p$ is determined by $x \mapsto f(w\, n(x))$, and the image of $\nu$ is a translation invariant measure on $\mathrm{Herm}_p^S(e)$, hence $c\lambda$ for some $c \ge 0$. This gives $\mu(f) = c \int f(w\, n(x))\, d\lambda(x)$. If $c = 0$ the first case holds, and otherwise the second. $\square$

### The residue of a reduced Siegel-Weil section

Let $V$ be a Hermitian space and $\mu_V$ a measure of covolume one on $M_{m_V \times n}(\mathbb{A}_E)$. A *Weil representation* of $G_n$ on the Schwartz functions on $M_{m_V \times n}(\mathbb{A}_E)$, for $\psi$ and $\chi$, is a homomorphism $\omega_V$ with
$$\begin{aligned} (\omega_V(m)\Phi)(x) &= \chi(\det a)\, |\det a|^{m_V/2}\, \Phi(xa), \qquad m = \mathrm{diag}(a, (a^*)^{-1}), \\ (\omega_V(n(b))\Phi)(x) &= \psi(\tfrac12 \operatorname{tr}(b \langle x, x \rangle))\, \Phi(x), \\ (\omega_V(w)\Phi)(x) &= \int \Phi(y)\, \psi(\operatorname{tr} \langle x, y \rangle)\, d\mu_V(y). \end{aligned}$$
These are the formulas of the [Weil representation](/learn/theta/#the-weil-representation) in the Schrödinger model. For a Schwartz $\Phi$ on $M_{m_B \times n}(\mathbb{A}_E)$ let $f_\Phi(g) = (\omega_B(g)\Phi)(0)$, the Siegel-Weil section. Recall the reduced section $R(f, g, \Omega)$ and the theta class $\mathrm{Th}(\psi, \chi, b_0)$ of the second section, now with $\rho = r$ and $p = t$, and the notation $y(z)$, $q(z)$ of the fifth section.

The next theorem has many inputs. Each is a statement on Schwartz functions, theta functions or measures that we take as given here. We list them for an $S$-idempotent $e$ with $S$ large enough:

- (Bumps) for each compact set $C$ of matrices integral off $S$ there are good Schwartz functions $\eta_i$ of one row, of compact support and with values in $[0, 1]$, such that $\eta_i$ equals $1$ at the $i$-th row of each point of $C$;
- (Majorants) each good Schwartz $\Phi$ has a good positive Schwartz majorant $\Phi_0$, and good Schwartz functions of compact support approximate $\Phi$ up to $\varepsilon \Phi_0$;
- (Fixed vectors) $\omega_V(u)\Phi = \Phi$ for good $\Phi$ and $u \in K^S$; and $\Omega(hu) = \Omega(h)$ for $u \in K^S$ when $\Omega \in \mathrm{Th}(\psi, \chi, b_0)$ and $\Omega(1, \cdot)$ is good;
- (Products) for $b_0$ diagonal invertible, the theta class contains $\Omega$ with $\Omega(1, \cdot)$ equal to the product of given Schwartz functions of the rows;
- (Fibres) for $2r < m_V$ there is a fibre measure on $\{x : \langle x, x \rangle = b_0\}$, finite on compact sets and invariant under $U(V)(\mathbb{A})$, that represents a Siegel-Weil type integral of Schwartz functions;
- (Cell values) $R(f_\Phi, 1, \Omega)(w\, n(x))$ equals the integral of $\Phi(z_1 \mid z_2)\, \overline{\Omega(1, y(z))}\, \psi(\tfrac12 \operatorname{tr}(x\, q(z)))$ against the fibre measure times a covolume one measure;
- (Riesz) a positive linear functional on a $*$-algebra of continuous functions of compact support that separates points is integration against a unique measure;
- (Approximate identity) $\mathrm{Herm}_t^S(e)$ carries an approximate identity whose Fourier transforms are nonnegative and tend to $0$ uniformly on closed sets of nonzero matrices $T$ with $eT = T$.

**Theorem 5.6.3 (Residue functional as an orbit integral).** Assume the conclusions of the theorem on idempotents, of the cell formula and of the inputs above. Let $\psi$ be an additive character, $\chi$ a Hecke character that satisfies the restriction condition for $r$, and assume $1 \le r < t$ and $r + 2 < 2t$. Let $\omega_B$ and $\omega_W$ be Weil representations of $G_n$ for $\psi$ and $\chi$, with $n = r + t$. Let $\mu$ be a residue functional on $G_t$ and $b_0 \in \mathrm{Herm}_r(E)$ diagonal invertible. Assume that $R(f_\Phi, 1, \Omega) \in \mathcal{R}_t$ for all $\Omega \in \mathrm{Th}(\psi, \chi, b_0)$ and all Schwartz $\Phi$. Then there is a finite $S_0$ such that for each finite $S \supseteq S_0$ and each $S$-idempotent $e$ there is an orbit measure $\nu$ for $(B, b_0, e)$ with
$$\mu\big(R(f_\Phi, 1, \Omega)\big) = \int \Phi(z_1 \mid z_2)\, \overline{\Omega(1, y(z))}\, d\nu(z)$$
for each Schwartz $\Phi$ good for $(S, e)$ and each $\Omega \in \mathrm{Th}(\psi, \chi, b_0)$ such that $\Omega(1, \cdot)$ is good for $(S, e)$ and has compact support.

Lean: `PositivityTheory.Rg.Rsw.Em.eisMeas`.

*Proof.* We give the route; the steps are lemmas that we take as given. Fix $S$ and $e$, and let $\Phi$ and $\Omega(1, \cdot)$ be good. By the fixed vector inputs, $f_\Phi$ and $\Omega$ are right invariant under $K^S$, so the reduced section $R = R(f_\Phi, 1, \Omega)$ is right invariant under $K^S$. The [Theorem 5.6.2](/entry/mu-cell/) on the cell formula gives $\mu(R) = 0$ for all such $R$, and then the zero measure works, or $\mu(R) = c \int R(w\, n(x))\, d\lambda(x)$ with $c > 0$. In the second case, insert the cell values: $R(w\, n(x))$ is a fibre integral with the phase $\psi(\tfrac12 \operatorname{tr}(x\, q(z)))$. Since $\Phi$ and $\Omega(1, \cdot)$ are good, this integral moves to the image of the fibre measure under $z \mapsto (ez_1, ez_2)$. Integrate in $x$ against the approximate identity. Its Fourier transforms are nonnegative and concentrate on $q(z) = 0$, and the positivity of $\mu$, the bumps and the majorants control the limit. The limit is a positive linear functional on the algebra spanned by the products $\Phi(z_1 \mid z_2)\, \overline{\Omega(1, y(z))}$. The product theta functions and the bumps make this algebra separate points. The Riesz input then gives $\nu$, and the uniqueness in it turns the symmetries of the construction into the invariance properties of an orbit measure. $\square$

**Remark 5.6.4 (Formalization).** The cell formula takes $S_0 = \emptyset$, so it holds for every finite $S$ ([MuCellOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/HermitianCellMeasures/MuCellOf.lean#L17)). In the last theorem the condition $r + 2 < 2t$ follows from $1 \le r < t$, so it adds nothing. The fibre measure represents an integral that we have not unfolded. We have not opened the lemmas of the two proofs on cells, fibres and approximate identities; the routes above follow the statements of these lemmas, which are the inputs listed.
