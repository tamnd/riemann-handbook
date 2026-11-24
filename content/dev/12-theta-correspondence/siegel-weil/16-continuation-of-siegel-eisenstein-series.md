---
title: Continuation of Siegel Eisenstein series
decls:
  - GlobalTheory.CompanionTheory.EpsteinMain.Hd.epMain_of_epConv
  - PositivityTheory.RgEis.Hd.epMain_of
  - PositivityTheory.RgEis.TF.testFun
  - PositivityTheory.RgEis.Hd.testFun
  - PositivityTheory.RgEis.MG.mirGen
  - PositivityTheory.RgEis.Hd.mirGen_of
  - PositivityTheory.RgEis.Hd.gallery_of
  - PositivityTheory.RgEis.So.sgOne_hd
  - PositivityTheory.RgEis.Hd.sgOne_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Continuation of Siegel Eisenstein series

The Siegel-Weil formulas of this chapter are identities at a point where the Siegel [Eisenstein series](/learn/automorphic-forms/#eisenstein-series) is defined by meromorphic continuation, not by its convergent sum. This section proves the continuation in the form the chapter needs. It is a wall crossing statement: the Eisenstein series is the value of a holomorphic family that agrees with the convergent series on a right half plane, and with a second Eisenstein series, composed with an intertwining operator, on a left half plane. The base case, rank one, comes from the Epstein zeta function of $\mathrm{GL}_n$ and the mirabolic subgroup, and the induction on the rank glues walls along a gallery of parabolic subgroups by tube domains. The result feeds the multiplicativity of Siegel Eisenstein series and, through it, the archimedean side of [every character](/step/every-character/).

### The Epstein zeta function

Let $k$ be a number field, $\iota$ a finite index set with $n = |\iota|$, $\Psi$ a Schwartz-Bruhat function on $\mathbb{A}_k^\iota$ and $\omega$ a [Hecke character](/learn/class-field-theory/#hecke-characters). For $x \in \mathbb{A}_k^\iota$ let
$$Z(\Psi, \omega, z, x) = \int_{\mathbb{A}_k^\times} \Psi(t x) \, \omega(t) \, |t|^z \, d^\times t$$
be the global zeta integral on the line through $x$. The Epstein zeta function is
$$\operatorname{Ep}(\Psi, \omega, z, m) = \sum_{\ell \in \mathbb{P}(k^\iota)} Z\bigl(\Psi, \omega, z, m^{-1} \xi_\ell\bigr),$$
with $\xi_\ell$ a representative of the line $\ell$ and $m \in \mathrm{GL}_\iota(\mathbb{A}_k)$. It converges for $\operatorname{Re} z > n$.

**Definition 4.16.1 (Epstein continuation).** A function $F(z, m)$ is an Epstein continuation of $(\Psi, \omega)$ if it is entire in $z$ for each $m$, jointly continuous, equal to $z(z - n) \operatorname{Ep}(\Psi, \omega, z, m)$ for $\operatorname{Re} z > n$, and bounded by $C(1 + |z|)^2$ on vertical strips, uniformly for $m$ in compact sets.

**Theorem 4.16.2 (Epstein zeta function).** For each number field $k$ there is $V > 0$ with the following property. For every $\iota$, every Schwartz-Bruhat $\Psi$ and every $\omega$ with $\omega^2 = 1$ there are Epstein continuations $F$ of $(\Psi, \omega)$ and $F'$ of $(\hat{\Psi}, \omega)$ with
$$F(z, m) = |\det m| \, F'\bigl(n - z, {}^t m^{-1}\bigr),$$
and, when $\omega = 1$,
$$\begin{aligned} F(0, m) &= n V \Psi(0), \\ F(n, m) &= n V |\det m| \, \hat{\Psi}(0). \end{aligned}$$

Lean: `GlobalTheory.CompanionTheory.EpsteinMain.Hd.epMain_of_epConv` (also `PositivityTheory.RgEis.Hd.epMain_of`, a second name).

*Proof.* This is Hecke's method. Write $\operatorname{Ep}(\Psi, \omega, z, m)$ as the Mellin transform over $\mathbb{A}_k^\times / k^\times$ of the theta series $\theta(t) = \sum_{\xi \in k^\iota \setminus 0} \Psi(t m^{-1} \xi)$, after folding the sum over lines with the units. Poisson summation on $k^\iota \subset \mathbb{A}_k^\iota$ gives
$$\theta(t) + \Psi(0) = |t|^{-n} |\det m| \bigl(\hat{\theta}(t^{-1}) + \hat{\Psi}(0)\bigr),$$
where $\hat{\theta}$ is the theta series of $\hat{\Psi}$ at ${}^t m^{-1}$. This makes $(\theta, \hat{\theta})$ a weak pair in the sense of the functional equation (`pairAt`). Split the Mellin integral at $|t| = 1$ and use the pair on the part $|t| < 1$. The result is an entire function plus the two polar terms $\Psi(0)/z$ and $\hat{\Psi}(0)/(z - n)$, each multiplied by the volume $V$ of the norm one ideles modulo $k^\times$ (`volChar_one_eq`). Multiplying by $z(z - n)$ gives the entire function $F$ (`entireForm`) and the values at $0$ and $n$. The functional equation is the symmetry of the split integral, and the strip bound comes from the rapid decay of $\theta$ away from the polar terms. $\square$

This is the theorem of Tate's thesis and of Godement and Jacquet for the standard $L$-function of the trivial representation, in the form used for the mirabolic Eisenstein series by Jacquet and Shalika.

### Test functions

**Theorem 4.16.3 (Test functions).** Let $k$ be a number field, $i_0 \in \iota$, $\omega$ with $\omega^2 = 1$, and $U$ a neighbourhood of $1$ in the standard maximal compact subgroup $K$ of $\mathrm{GL}_\iota(\mathbb{A}_k)$. There are Schwartz-Bruhat $\Psi$ on $\mathbb{A}_k^\iota$ and $\Psi_1$ on $\mathbb{A}_k$, and a continuous $\psi$ on $K$ with $\psi(1) = 1$, such that the following hold.

1. $\Psi(t \kappa^{-1} e_{i_0}) = \Psi_1(t) \psi(\kappa)$ for $t \in \mathbb{A}_k$ and $\kappa \in K$.
2. If $\psi(\kappa) \ne 0$ then $\kappa = p u$ with $p$ in the stabiliser of the line $k e_{i_0}$ and $u \in U$, and $\psi(\kappa) = \omega(\operatorname{bdet} p) |\psi(\kappa)|$.
3. $\psi(p \kappa) = \omega(\operatorname{bdet} p) \psi(\kappa)$ for $p$ in the stabiliser.
4. The zeta integral $Z(\Psi_1, \omega, z)$ is nonzero for some $z$ with $\operatorname{Re} z > n + 1$, and when $\omega = 1$ it is nonzero at every real $x > 1$.

Here $\operatorname{bdet} p$ is the diagonal entry of $p$ at $i_0$.

Lean: `PositivityTheory.RgEis.TF.testFun` (also `PositivityTheory.RgEis.Hd.testFun`, a second name).

*Proof.* Choose $\psi$ as the function $\kappa \mapsto \omega(\operatorname{bdet} p) \beta(u)$ on the set $\{p u\}$ of the decomposition in (2), with $\beta$ a bump function on $U$ with $\beta(1) = 1$, and extend by zero; this is well defined and continuous if $U$ is small. Define $\Psi$ on the vectors $t \kappa^{-1} e_{i_0}$ by (1) and extend it to a Schwartz-Bruhat function by a cut off in the transverse directions. For $\Psi_1$ take the standard Gaussian times the characteristic function of the integers, twisted by $\omega$ at the ramified places; its zeta integral is an $L$-function times a nonzero factor, which is nonzero in the half plane of convergence, and for $\omega = 1$ it is the completed Dedekind zeta function, which is positive on $x > 1$. $\square$

### The mirabolic wall

Let $G$ be a locally compact group with a continuous homomorphism $\pi \colon G \to \mathrm{GL}_\iota(\mathbb{A}_k)$, a discrete subgroup $\Gamma$ and a compact $K$, and let $P$ and $P'$ be parabolic subgroups with characters $c$ and heights $\eta$ and $\eta'$. A wall from $P$ to $P'$ with shift $\beta$ is a holomorphic family $H(z, g)$ of operators on the sections of a finite dimensional representation $\rho$ of $K$, with an entire $D \ne 0$, an operator $\operatorname{Op}(z)$ and $R \ge 0$, such that
$$\begin{aligned} H(z, g) &= D(z) \, E_P(z \eta, g) \quad (\operatorname{Re} z > R), \\ H(z, g) &= E_{P'}\bigl(\beta - z \eta', g\bigr) \circ \operatorname{Op}(z) \quad (\operatorname{Re} z < -R), \end{aligned}$$
where $E_P$ is the Eisenstein series induced from $P$. A first wall also fixes the value at $z = 0$ as a nonzero multiple of the section, and a last wall has $D$ vanishing simply at $N$ with $H(N, \cdot)$ a section.

**Theorem 4.16.4 (Mirabolic generation).** Let $n \ge 2$, and let the data $(\pi, \Gamma, K, i_0, i_1, \omega, c, \eta, \eta', l)$ satisfy $\mathrm{MirData}$: $\pi$ maps $\Gamma$ to rational points and $K$ into $K$ up to a diagonal twist, $\Gamma$ acts transitively on the rational flags of the stabilisers of $\{i_0\}$ and $\{i_1\}^c$, and $c$, $\eta$, $\eta'$ and $l$ are given on these stabilisers by $\omega \circ \operatorname{bdet}$ and the logarithm of $|\operatorname{bdet}|$ or $|\det|$. Then there is a wall from the stabiliser of $i_0$ to the stabiliser of $\{i_1\}^c$ with shift $l + n \eta'$. If $\omega = 1$ and $c = 1$ there are also a first wall and a last wall at $N = n$.

Lean: `PositivityTheory.RgEis.MG.mirGen` (also `PositivityTheory.RgEis.Hd.mirGen_of`, a second name).

*Proof.* The Eisenstein series induced from the mirabolic stabiliser of $i_0$ is an average over $\Gamma$ of the Epstein zeta function: the sum over lines $\mathbb{P}(k^\iota)$ is the sum over $\Gamma$ modulo the stabiliser, and the test function of the previous theorem makes the zeta integral on each line factor as $Z(\Psi_1, \omega, z) \psi$. Divide by $Z(\Psi_1, \omega, z)$, which is nonzero, so that $D(z) = z(z - n) Z(\Psi_1, \omega, z)$. The continuation of the Epstein zeta function gives $H$, and its functional equation, with $\Psi$ replaced by $\hat{\Psi}$ and $m$ by ${}^t m^{-1}$, gives the left half plane in terms of the stabiliser of $\{i_1\}^c$. When $\omega = 1$ the values at $0$ and $n$ give the first and last walls. In Lean the assembly runs through the side term identity, the unfolding of averages and the master identity of the mirabolic generation lemma. $\square$

### Galleries and the induction

The induction on the rank crosses several walls in turn. To glue the continuations across them one uses holomorphic functions of two variables on tube domains.

**Theorem 4.16.5 (Gallery).** Assume the section law, uniqueness of holomorphic continuation on tubes, the tube chain gluing and the crossing law. Let $S$ be a parabolic subgroup with height $h$ and $A, B \le S$ parabolic subgroups with heights $a$ and $h + b$. Suppose the Eisenstein series of $S$, $A$ and $B$ converge in the stated ranges, and that there are a first wall in $S$ from $A$ to $B$, three walls inside $Q_2$, $S$ and $Q_1$ with the stated shifts, and a last wall in $S$ at $N$. Then there is a wall from $S$ to $S$ with height $h$ and shift $N h$.

Lean: `PositivityTheory.RgEis.Hd.gallery_of`.

*Proof.* Each wall is a holomorphic function of one variable $z$. The crossing law extends it to a function of two variables $(z, y)$ on a tube $\{(z, y) : (\operatorname{Re} z, \operatorname{Re} y) \in \Omega\}$ over an open convex $\Omega$, by summing over $\Gamma \cap Q$ against the height $y$. Two neighbouring walls agree on the tube over the overlap of their domains, by the shared Eisenstein series. The tube chain law glues the five functions to one holomorphic function on $\mathbb{C}^2$, after multiplying by $\exp(z^2 + y^2)$ to control growth; its hypothesis that every point of $\mathbb{R}^2$ is a midpoint of two points of the domains is the convex hull condition of Bochner's tube theorem. Uniqueness on tubes makes the gluing well defined. Restricting to a line gives the wall from $S$ to $S$. $\square$

**Theorem 4.16.6 (Rank one).** Assume the section law, the wall law, the scaling law, goodness of the standard section, the local global dictionary, the constant multiplier law, the group topology, the block determinant law, the extension and parabolic laws, and mirabolic generation. Then $\mathrm{Sg}$ holds for every CM pair $(\sigma, \chi)$ and every $\iota$ with $|\iota| = 1$: for each $\varepsilon = \pm 1$ and each finite dimensional representation $\rho$ of $K$, the Siegel Eisenstein series of $U_\varepsilon(1, 1)$ has a wall from the Siegel parabolic to itself with shift $n$ times the height.

Lean: `PositivityTheory.RgEis.So.sgOne_hd` (also `PositivityTheory.RgEis.Hd.sgOne_of`, a second name).

*Proof.* For $|\iota| = 1$ the Siegel parabolic of $U_\varepsilon(1, 1)$ is a Borel subgroup, and the group is isogenous to a form of $\mathrm{GL}_2$ over $F$ twisted by $E$. The base change to $\mathrm{GL}_2$ over $E$ carries the Siegel Eisenstein series to a mirabolic Eisenstein series (`baseCM`), and the needed rationality, integrality and archimedean properties of the base change are separate lemmas (`bFix`, `brat`, `bInt`, `bInf`). The dictionary relates the two Haar measures and heights (`blg_of_dict`). The Iwasawa decomposition and the compactness of $K$ (`jiwa`, `jcpt`) let mirabolic generation apply, and its wall is the wall for $\mathrm{Sg}$. $\square$

The induction step $\mathrm{SgStep}$ deduces $\mathrm{Sg}$ for $\iota$ from $\mathrm{Sg}$ for all smaller index sets and the mirabolic law, using a gallery; with the rank one case, strong induction gives $\mathrm{SgAll}$ (`sgAll_of`), and $\mathrm{SgAll}$ gives the multiplicativity of Siegel Eisenstein series.

**Remark 4.16.7 (Formalization).** The proof of `epMain_of_epConv` begins with `intro _`, so its hypothesis $\mathrm{EpConv}$ is not used ([ContinuousOnThetaCFunLtr.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinSeries/SiegelEisensteinHalfPlane/SchwartzBruhatMajorants/ContinuousOnThetaCFunLtr.lean#L460)), and yet `Hd.epMain_of` keeps the argument. Mirabolic generation does use $\mathrm{EpConv}$, through the zeta integral of the Epstein series ([MirGen.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinSeries/SiegelEisensteinHalfPlane/MirabolicGenerators/MirGen.lean#L22)). The rank one proof `sgOne_hd` ignores its arguments $\mathrm{WallLaw}$ and $\mathrm{DictInf}$ ([SgOneHd.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinSeries/SiegelEisensteinHalfPlane/SchwartzBruhatMajorants/SgOneHd.lean#L23)). The names `Hd.*` in [SiegelMultOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinSeries/SiegelEisensteinHalfPlane/SchwartzBruhatMajorants/SiegelMultOf.lean#L49) are second names, at lines 49 to 72, and `Hd.gallery_of` is `GlobalTheory.T.gallery_of_tubes_and_crossing`. The predicates $\mathrm{EpConv}$, $\mathrm{EpMain}$, $\mathrm{TestFun}$ and $\mathrm{MirGen}$ are in [IsEpCont.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinSeries/SiegelEisensteinContinuation/IsEpCont.lean#L53), and $\mathrm{IdTube}$, $\mathrm{TubeChain}$, $\mathrm{Cross}$ and $\mathrm{Gallery}$ in [StripEntire.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinSeries/SiegelEisensteinContinuation/StripEntire.lean#L162). $\mathrm{SgOne}$ is in [DictInf.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinSeries/SiegelEisensteinContinuation/DictInf.lean#L57) and $\mathrm{SgStep}$ in [ConvGrOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinSeries/SiegelEisensteinContinuation/ConvGrOf.lean#L219). The test function theorem is in [TestFun.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinSeries/SiegelEisensteinHalfPlane/UnitTestFunctions/TestFun.lean#L18).
