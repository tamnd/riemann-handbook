---
title: Complex and formal geometry
decls:
  - UpperTheory.LiteratureTheorems.good_chern_weil_of_literature
  - UpperTheory.LiteratureTheorems.l2_extension_log_canonical_of_literature
  - UpperTheory.LiteratureTheorems.formal_algebraisation_of_literature
  - UpperTheory.LiteratureTheorems.semi_abelian_lie_seminegative_of_literature
  - UpperTheory.LiteratureTheorems.siegel_toroidal_integral_of_literature
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Complex and formal geometry

This section states five results from complex geometry and from the geometry of abelian schemes: Mumford's theorem that good metrics compute Chern numbers, an $L^2$ extension theorem of Ohsawa-Takegoshi type, Grothendieck's existence theorem, the seminegativity of the Lie algebra of a semi-abelian scheme over a curve, and the existence of smooth projective toroidal compactifications of Siegel moduli schemes over $\mathbb{Z}[\zeta_n, 1/n]$. All five are inputs to the volume bound for the Hodge bundle. The first three are fields of the bundle of [published Hodge bundle theorems](/step/published-results-arithmetic/). The last two are direct arguments of the step [EveryCharacter from the literature](/step/every-character-of-literature/). Background is in [Chern-Weil forms](/learn/positivity-resolution/#chern-weil-forms), [L2 estimates](/learn/positivity-resolution/#l2-estimates), [formal functions and Grothendieck's existence theorem](/learn/commutative-algebra/#formal-functions-and-grothendiecks-existence-theorem), [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction) and [toroidal and minimal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications).

### Good metrics

Let $X$ be a smooth projective variety over a field $F$ with an embedding $F \to \mathbb{C}$, let $D \subset X$ be a divisor with normal crossings, and let $\mathcal{E}$ be a vector bundle on $X$ with a Hermitian metric $h$ on $\mathcal{E}|_{X \setminus D}$. Mumford calls $h$ *good* if, near each point of $D$, the entries of $h$ and $h^{-1}$ grow at most like a power of $\log$ of the distance to $D$, and the connection and curvature forms have Poincaré growth.

**Theorem 1.5.1 (Mumford).** The following two statements hold.

1. Let $\mathcal{E}$ be given by a frame over $X$, with a good metric $h$ on an open set $U = X \setminus D$. Let $R$ be a polynomial in the Chern classes. Then the Chern form $R(c(\mathcal{E}, h))$ is integrable on $U(\mathbb{C})$, and its integral is the Chern number $\int_X R(c(\mathcal{E}))$, computed on a flag refinement of the frame through the Chern roots.
2. (Splitting principle.) Let $Y \to X$ be the flag bundle of $\mathcal{E}$ in characteristic $0$, and let $Q$ be a polynomial in the Chern roots whose antisymmetrisation is $R(c) \cdot \Delta$, where $\Delta$ is the discriminant of the roots. Then the intersection number of $Q$ on $Y$ equals the intersection number of $R(c)$ times the class of a point of the fibre.

Lean: `UpperTheory.LiteratureTheorems.good_chern_weil_of_literature`.

Part 1 is Mumford, *Hirzebruch's proportionality theorem in the non-compact case* (Invent. Math. 42, 1977), §1. Part 2 is the push-forward formula for flag bundles. See [Mumford's proportionality theorem](/learn/abelian-varieties/#mumfords-proportionality-theorem).

*Proof.* We take both parts from the literature. In the development they are [Theorem 5.3.6 of Volume 6](/entry/good-chern-weil/). $\square$

### $L^2$ extension

Let $Y$ be a compact complex manifold of dimension $n \geq 1$ that carries a line bundle $H$ with positive curvature. Let $E$ and $L$ be Hermitian line bundles, and let $K$ be the canonical bundle. Let $s = (s_1, \dots, s_n)$ be sections of $L$ whose common zero set $Z$ is finite, with nonzero Jacobian $J_s(P)$ at each $P \in Z$, and with $|s|^2 \leq 1$. Put $\psi = n \log |s|^2$. For $f : Z \to \mathbb{C}$ and $P \in Z$ put

$$r(P) = \frac{|f(P)|^2}{|J_s(P)|^2} \, e^{-\phi_E(P) + n \phi_L(P)},$$

where $\phi_E, \phi_L$ are the local weights of the metrics, and let $c_n = 2^{n+1} \pi^n / (n-1)!$.

**Theorem 1.5.2 (Ohsawa-Takegoshi).** In this setting let $\delta > 0$, and assume that $\phi_E + \alpha \psi$ is plurisubharmonic outside $Z$ for every $\alpha \in [1, 1 + \delta]$. Then every $f : Z \to \mathbb{C}$ extends to a section $F$ of $K + E$ with $F = f$ on $Z$ and

$$\int_Y \frac{2^n \, |F|^2 \, e^{-\psi}}{1 + (\delta \psi)^2} \, d\mu \leq \frac{34}{\delta} \, c_n \sum_{P \in Z} r(P).$$

Lean: `UpperTheory.LiteratureTheorems.l2_extension_log_canonical_of_literature`.

This is the extension theorem of Ohsawa and Takegoshi (Math. Z. 195, 1987) in the form of Manivel (Math. Z. 212, 1993), with the weight $1 / (1 + (\delta \psi)^2)$ and a numerical constant, applied to the zero-dimensional subvariety $Z$.

*Proof.* We take the result from the literature. In the development it is [Theorem 10.5.3 of Volume 3](/entry/l2-extension-log-canonical-prime/). $\square$

### Grothendieck's existence theorem

Let $R$ be a noetherian ring, complete for the $I$-adic topology of an ideal $I$. For a scheme $X$ over $R$ write $X_e = X \times_R R / I^{e+1}$.

**Theorem 1.5.3 (Grothendieck).** The following two statements hold.

1. Let $X$ be proper over $R$, and let $Z$ be separated, quasi-compact and locally of finite type over $R$. Let $f_e : X_e \to Z$ be morphisms over $R$, compatible with the inclusions $X_e \to X_{e+1}$. Then there is a unique morphism $g : X \to Z$ over $R$ with $g|_{X_e} = f_e$ for all $e$.
2. Let $Y_e$ be proper schemes over $R / I^{e+1}$ with $Y_{e+1} \times R / I^{e+1} \cong Y_e$, and let $N_e$ be line bundles on $Y_e$, compatible under pullback, with $N_0$ relatively ample. Then there are a proper scheme $X$ over $R$, a relatively ample line bundle $M$ on $X$ and compatible isomorphisms $X_e \cong Y_e$ with $M|_{X_e} \cong N_e$.

Lean: `UpperTheory.LiteratureTheorems.formal_algebraisation_of_literature`.

Part 1 is EGA III$_1$, Théorème 5.4.1. Part 2 is EGA III$_1$, Théorème 5.4.5.

*Proof.* We take both parts from EGA. In the development they are [Theorem 4.7.3 of Volume 6](/entry/formal-thickening-formal-algebraisation/). $\square$

### Semi-abelian schemes over curves

**Theorem 1.5.4 (Seminegativity of the Lie algebra).** Let $k$ be a field of characteristic $0$, and let $C$ be a smooth, projective, geometrically connected curve over $k$. Let $G$ be a semi-abelian scheme over $C$, and let $W$ be a vector bundle of rank $r$ on $C$ with an injective map $W \to \mathrm{Lie}(G)$. Then

$$\deg \det W \leq 0.$$

Lean: `UpperTheory.LiteratureTheorems.semi_abelian_lie_seminegative_of_literature`.

Equivalently, the dual $\omega_G = \mathrm{Lie}(G)^\vee$ is nef: each of its quotient bundles has degree at least $0$. This is a theorem of Moret-Bailly (*Pinceaux de variétés abéliennes*, Astérisque 129, 1985) and of Faltings and Chai (*Degeneration of Abelian Varieties*, Chapter V).

*Proof.* We take the result from the literature. In the development it is [Theorem 5.4.9 of Volume 6](/entry/semi-abelian-lie-seminegative/). $\square$

### Toroidal compactifications

For $n \geq 3$ let $\mathcal{A}_{g,n}$ be the moduli scheme of principally polarised abelian schemes of dimension $g$ with a full level $n$ structure, over $\mathbb{Z}[\zeta_n, 1/n]$. Let $\omega$ be the Hodge line bundle, the determinant of $\mathrm{Lie}^\vee$ of the universal abelian scheme.

**Theorem 1.5.5 (Faltings-Chai).** Let $g \geq 1$. There is a polarised admissible cone decomposition $\Sigma$ for $\mathrm{GL}_g(\mathbb{Z})$ such that, for each odd $n \geq 3$, there is a scheme $\overline{\mathcal{A}}_{g,n}$ over $\mathbb{Z}[\zeta_n, 1/n]$ with an open immersion $j : \mathcal{A}_{g,n} \to \overline{\mathcal{A}}_{g,n}$ and these properties.

1. $\overline{\mathcal{A}}_{g,n}$ is projective and smooth of relative dimension $g(g+1)/2$, and $\mathcal{A}_{g,n}$ is dense in each fibre.
2. The universal abelian scheme extends to a semi-abelian scheme $G$ over $\overline{\mathcal{A}}_{g,n}$ of relative dimension $g$, and the locus where $G$ is abelian is $\mathcal{A}_{g,n}$.
3. Near each boundary point, $\overline{\mathcal{A}}_{g,n}$ has a chart given by $\Sigma$, as in Mumford's construction.
4. Some power $\omega^N$ is generated by global sections, and there are an effective Cartier divisor $B$ supported on the boundary and $k_0$ with $\omega^{N k}(-B)$ ample for all $k \geq k_0$.

Lean: `UpperTheory.LiteratureTheorems.siegel_toroidal_integral_of_literature`.

This is Faltings and Chai, *Degeneration of Abelian Varieties*, Chapters IV and V, for the projective toroidal compactifications given by a polarisation function on the fan.

*Proof.* We take the result from Faltings and Chai. In the development it is [Theorem 9.1.9 of Volume 5](/entry/siegel-toroidal-integral-holds/). $\square$

**Remark 1.5.6 (Formalization).** All five theorems take the record of open statements as an argument and do not use it. They are the terms `GlobalTheory.GoodMetric.goodChernWeil`, `GlobalTheory.l2ExtensionLogCanonical'`, `PositivityTheory.FormalThickening.formalAlgebraisation`, `GlobalTheory.Nef.semiAbelianLieSeminegative` and `GlobalTheory.siegelToroidalIntegral_holds` ([EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L381), lines 381, 395, 451, 499 and 509). The statements are at [MumfordProportionality.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/MumfordProportionality.lean#L30), [L2ExtensionLogCanonical.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/L2ExtensionLogCanonical.lean#L32), [FormalAlgebraisation.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/FormalAlgebraisation.lean#L17), [InterNumDetNonposSplitTorus.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/InterNumDetNonposSplitTorus.lean#L23) and [SiegelToroidalIntegral.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/SiegelToroidalIntegral.lean#L145). The good metric statement is written with frames `Fr`, the predicates `IsMetricOn`, `IsGood`, `HasChernIntegral` and the intersection polynomial `interPoly`; we did not unfold them, and our statement follows the names. The $L^2$ statement is written on a compact space with a weighted atlas, not on a complex manifold; we did not unfold the atlas, its Levi forms or its measure. The Siegel statement asks only for odd $n$, while Faltings and Chai work with all $n \geq 3$. Its charts `HasChart` and the cone decomposition `IsPolFan` were not unfolded. In Grothendieck's theorem, part 1 asks $Z$ to be locally of finite type, separated and quasi-compact, and part 2 asks the line bundles to be compatible up to isomorphism.
