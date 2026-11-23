---
title: Crystalline lattices are prismatic F-crystals
decls:
  - GlobalTheory.BSP.bhattScholzeIntegral
  - GlobalTheory.T.crystallineLattice_prismaticFCrystal_perfectPrism
  - GlobalTheory.BSP.clause1_perfectPrism
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Crystalline lattices are prismatic F-crystals

This section proves the integral comparison of Bhatt and Scholze: a $G_K$-stable lattice in a crystalline representation comes from a prismatic F-crystal over $\mathcal{O}_K$, and an equivariant map of such lattices comes from a unique map of F-crystals (B. Bhatt and P. Scholze, "Prismatic F-crystals and crystalline Galois representations", *Camb. J. Math.* 11 (2023)). The theorem is the input of [the literature entry](/entry/bhatt-scholze-integral-of-literature/). The proof has two steps. First, a change of model reduces both parts from an arbitrary $A_{\mathrm{inf}}$-prism to the standard one. Second, at the standard prism, the F-crystal is built from a Breuil-Kisin datum and a stratified $\varphi$-module; the next section constructs F-crystals from such modules. We use the period rings of [[Fontaine's period rings|K6HW8YWCQJ]] and the [lattices of the Background](/learn/padic-hodge/#lattices-wach-breuil-kisin-and-prismatic-f-crystals).

Fix a prime $\ell$ and a finite extension $K$ of $\mathbb{Q}_\ell$ in a fixed algebraic closure. Let $\mathbb{C}_\ell$ be the completion, $\mathcal{O}_{C}$ its ring of integers, $\mathcal{O}_{C}^\flat$ the tilt, $C^\flat$ its fraction field, $A_{\mathrm{inf}} = W(\mathcal{O}_C^\flat)$ with Fontaine's map $\theta : A_{\mathrm{inf}} \to \mathcal{O}_C$, and $\iota : A_{\mathrm{inf}} \to W(C^\flat)$ the inclusion. Both rings carry the Frobenius $\varphi$ and an action of $G_{\mathbb{Q}_\ell}$.

**Definition 6.13.1 (Prism over $\mathcal{O}_K$).** A *prism over $\mathcal{O}_K$* is a ring $A$ with a $\delta$-structure $\delta$ and Frobenius $\varphi(a) = a^\ell + \ell\,\delta(a)$, an invertible ideal $I \subseteq A$ and a ring map $\mathcal{O}_K \to A/I$, such that $A$ is complete for the $(\ell) + I$-adic topology, $\ell \in I + \varphi(I)A$, and the $\ell$-power torsion of $A/I$ is killed by a fixed power of $\ell$. A *map of prisms* $f : (A, I) \to (A', I')$ is a ring map that commutes with $\delta$, maps $I$ into $I'$ and is compatible with the maps from $\mathcal{O}_K$.

Lean: `GlobalTheory.Prism.Obj` (also `GlobalTheory.Prism.Hom`, the maps).

A semilinear map $u : M \to N$ over a ring map $A \to B$ is a *base change* if every semilinear map $M \to Q$ to a $B$-module factors as $w \circ u$ for a unique $B$-linear $w : N \to Q$. Equivalently, the linearization $B \otimes_A M \to N$ is an isomorphism.

**Definition 6.13.2 (Prismatic F-crystal).** A *prismatic F-crystal* $E$ over $\mathcal{O}_K$ assigns to each prism $P = (A, I)$ a finite projective $A$-module $E(P)$, and to each map of prisms $f : P \to P'$ a base change $E(f) : E(P) \to E(P')$ over $f$, with $E(\mathrm{id}) = \mathrm{id}$ and $E(g \circ f) = E(g) \circ E(f)$. For each $d \in I$ it gives a base change
$$\Phi_{P,d} : E(P) \to E(P)[1/d]$$
over $A \xrightarrow{\varphi} A \to A[1/d]$. These are natural: if $\Phi_{P,d}(x) = m/d^k$ and $\Phi_{P',d'}(E(f)x) = n/d'^j$, then $(f(d)\,d')^r\big(d'^j E(f)(m) - f(d)^k n\big) = 0$ for some $r$. A *map of F-crystals* $u : E \to E'$ is a family of $A$-linear maps $u_P : E(P) \to E'(P)$ with $u_{P'} \circ E(f) = E'(f) \circ u_P$, and with $\Phi_{P,d}(u_P x) = u_P(m)/d^k$ whenever $\Phi_{P,d}(x) = m/d^k$.

Lean: `GlobalTheory.Prism.FCrys` (also `GlobalTheory.Prism.FHom`, the maps).

**Definition 6.13.3 ($A_{\mathrm{inf}}$-prism and realisation).** Let $P = (A, I)$ be a prism over $\mathcal{O}_K$ and $e : A \to A_{\mathrm{inf}}$ a ring isomorphism. The pair $(P, e)$ is an *$A_{\mathrm{inf}}$-prism* if $e \circ \varphi = \varphi \circ e$, $I = \ker(\theta \circ e)$, and $\theta(e(a))$ is the image of $x$ in $\mathcal{O}_C$ whenever $a \bmod I$ is the image of $x \in \mathcal{O}_K$. Then every $g \in G_K$ gives a map of prisms $g_P : P \to P$ with $e \circ g_P = g \circ e$. The *standard* $A_{\mathrm{inf}}$-prism $P_{\mathrm{st}}$ is $A_{\mathrm{inf}}$ with $I = \ker \theta$ and $e = \mathrm{id}$. Let $T$ be a $\mathbb{Z}_\ell$-module and $\rho : G_K \to \mathrm{End}_{\mathbb{Z}_\ell}(T)$ a map. An F-crystal $E$ with a map
$$j : E(P) \to W(C^\flat) \otimes_{\mathbb{Z}_\ell} T,$$
semilinear over $\iota \circ e$, *realises* $(T, \rho)$ at $(P, e)$ if $(P, e)$ is an $A_{\mathrm{inf}}$-prism and:

1. $j$ is a base change;
2. for $0 \neq d \in I$, if $\Phi_{P,d}(x) = m/d^k$, then $\iota(e(d))^k\,(\varphi \otimes 1)(j(x)) = j(m)$;
3. $j(E(g_P)\,x) = (g \otimes \rho(g))(j(x))$ for every $g \in G_K$.

Lean: `GlobalTheory.Prism.IsAinf` (also `GlobalTheory.Prism.Realises`, the realisation).

The second condition says that $j$ takes the Frobenius of $E$ to $\varphi \otimes 1$, and the third says that $j$ is $G_K$-equivariant. So a realisation identifies $W(C^\flat) \otimes_{A} E(P)$ with $W(C^\flat) \otimes T$ as étale $\varphi$-modules with $G_K$-action.

**Theorem 6.13.4 (Bhatt-Scholze integrality).** Let $\ell$ be a prime, $K$ a finite extension of $\mathbb{Q}_\ell$ and $(P_0, e)$ an $A_{\mathrm{inf}}$-prism over $\mathcal{O}_K$.

1. Let period data be given that are tied to Fontaine's rings. Let $V$ be a finite-dimensional $\mathbb{Q}_\ell$-representation of $G_K$ with continuous orbit maps that is crystalline for these period data, and $T \subseteq V$ a $G_K$-stable $\mathbb{Z}_\ell$-lattice. Then there is an F-crystal $E$ with a map $j$ that realises $T$ at $(P_0, e)$.
2. Let $(T, \rho)$ and $(T', \rho')$ be $\mathbb{Z}_\ell$-modules with maps from $G_K$, and $(E, j)$, $(E', j')$ realisations of them at $(P_0, e)$. For every $\mathbb{Z}_\ell$-linear $f : T \to T'$ with $f \circ \rho(g) = \rho'(g) \circ f$ for all $g$, there is a unique map $u : E \to E'$ of F-crystals with $j' \circ u_{P_0} = (1 \otimes f) \circ j$.

Lean: `GlobalTheory.BSP.bhattScholzeIntegral`.

*Proof.* We use three results proved elsewhere in this development. (a) There is a map of prisms $a : P_0 \to P_{\mathrm{st}}$ such that for every F-crystal $M$, the map $M(a)$ is bijective, every realisation $j_0$ of $(T, \rho)$ at $P_{\mathrm{st}}$ gives a realisation at $(P_0, e)$, and every realisation $j$ at $(P_0, e)$ has the form $j = j_0 \circ M(a)$ for a realisation $j_0$ at $P_{\mathrm{st}}$. (b) If $(M, j_0)$ and $(M', j_0')$ realise $(T, \rho)$ and $(T', \rho')$ at $P_{\mathrm{st}}$ and $f$ is equivariant, there is a map $u : M \to M'$ with $j_0' \circ u_{P_{\mathrm{st}}} = (1 \otimes f) \circ j_0$. (c) If $(M', j_0')$ realises $(T', \rho')$ at $P_{\mathrm{st}}$ and two maps $u, u' : M \to M'$ satisfy $j_0' \circ u_{P_{\mathrm{st}}} = j_0' \circ u'_{P_{\mathrm{st}}}$, then $u = u'$.

Part 1. The next Theorem gives $E$ and a realisation $j_0$ of $T$ at $P_{\mathrm{st}}$. By (a), $E$ also realises $T$ at $(P_0, e)$.

Part 2. By (a), write $j = j_0 \circ E(a)$ and $j' = j_0' \circ E'(a)$ with realisations $j_0$, $j_0'$ at $P_{\mathrm{st}}$. By (b) there is $u$ with $j_0' \circ u_{P_{\mathrm{st}}} = (1 \otimes f) \circ j_0$. For $x \in E(P_0)$, since $u$ commutes with the transition maps,
$$j'(u_{P_0} x) = j_0'(E'(a)\,u_{P_0} x) = j_0'(u_{P_{\mathrm{st}}} E(a) x) = (1 \otimes f)(j_0(E(a) x)) = (1 \otimes f)(j(x)).$$
For uniqueness, let $u'$ satisfy $j' \circ u'_{P_0} = (1 \otimes f) \circ j$. Every $y \in E(P_{\mathrm{st}})$ is $E(a)(x)$ for some $x$, since $E(a)$ is bijective. The computation above, read for $u'$ and for $u$, gives $j_0'(u'_{P_{\mathrm{st}}} y) = (1 \otimes f)(j(x)) = j_0'(u_{P_{\mathrm{st}}} y)$. By (c), $u' = u$. $\square$

The F-crystal of Part 1 is built at the standard prism from a Breuil-Kisin presentation of $\mathcal{O}_K$. Let $W = W(\mathbb{F}_{\ell^a})$ and $\mathfrak{S} = W[[X]]$, with the Frobenius that is the Frobenius of $W$ on coefficients and $X \mapsto X^\ell$.

**Definition 6.13.5 (Breuil-Kisin datum).** A *Breuil-Kisin datum* for $K$ is an $a \geq 1$, a monic Eisenstein polynomial $E \in W[X]$ of positive degree (its lower coefficients are divisible by $\ell$, its constant coefficient is $\ell$ times a unit, and some coefficient of index prime to $\ell$ is nonzero), an isomorphism $\mathcal{O}_K \cong \mathfrak{S}/(E)$ such that $\delta(E)$ is a unit and $\mathfrak{S}$ is $(\ell, E)$-adically complete, an element $\varpi^\flat \in \mathcal{O}_C^\flat$, and a ring map $\mathrm{ev} : \mathfrak{S} \to A_{\mathrm{inf}}$ with $\mathrm{ev}(X) = [\varpi^\flat]$. The map $\mathrm{ev}$ is the natural map on $W$, commutes with $\varphi$, sends $E$ to a generator of $\ker \theta$ and is compatible with the maps from $\mathcal{O}_K$, and $G_K$ fixes the image of $W$. The *Breuil-Kisin prism* is $(\mathfrak{S}, (E))$, and $\mathrm{ev}$ is a map of prisms from it to $P_{\mathrm{st}}$.

Lean: `GlobalTheory.BSP.BK`.

**Definition 6.13.6 (Stratified $\varphi$-module).** Let a Breuil-Kisin datum and $d \in \mathbb{N}$ be given. A *stratified $\varphi$-module of rank $d$* consists of $a', b \in \mathbb{N}$, matrices $A, A' \in M_d(\mathfrak{S})$ with $AA' = E^b$, and for each prism $B$ and maps $f, g$ from the Breuil-Kisin prism to $B$ a matrix $\varepsilon(f, g) \in M_d(B)$, such that $\varepsilon(f, f) = 1$, $\varepsilon(f, g)\,\varepsilon(g, h) = \varepsilon(f, h)$, $\varepsilon$ is natural in $B$, and
$$g(E)^{a'}\,A^f\,\varphi(\varepsilon(f, g)) = f(E)^{a'}\,\varepsilon(f, g)\,A^g,$$
where $A^f$ is $A$ with $f$ applied to its entries. A *frame* of an F-crystal $M$ by it is a basis $e_1, \dots, e_d$ of $M(\mathfrak{S}, (E))$ with $M(g)(e_j) = \sum_i \varepsilon(f, g)_{ij}\,M(f)(e_i)$ for all $f, g$, and $\Phi_E(e_j) = \big(\sum_i A_{ij} e_i\big)/E^{a'}$. A matrix $U \in M_d(W(C^\flat))$ *realises* the module for a matrix representation $\rho$ of $G_K$ over $\mathbb{Z}_\ell$ if $U$ is invertible, $\mathrm{ev}(E)^{a'}\varphi(U) = U A^{\mathrm{ev}}$ and $\rho(g)\,g(U) = U\,\varepsilon(\mathrm{ev}, g \circ \mathrm{ev})$ for $g \in G_K$.

Lean: `GlobalTheory.BSP.Strat` (also `GlobalTheory.BSP.Framed`, the frame, and `GlobalTheory.BSP.MReal`, the realising matrix).

**Theorem 6.13.7 (Crystalline lattices at the standard prism).** Let period data be given that are tied to Fontaine's rings, let $V$ be a finite-dimensional $\mathbb{Q}_\ell$-representation of $G_K$ with continuous orbit maps that is crystalline for these period data, and $T \subseteq V$ a $G_K$-stable lattice. Then there is an F-crystal $M$ with a map $j$ that realises $T$ at $P_{\mathrm{st}}$.

Lean: `GlobalTheory.BSP.clause1_perfectPrism` (also `GlobalTheory.T.crystallineLattice_prismaticFCrystal_perfectPrism`, a second name).

*Proof.* The lattice $T$ is free of finite rank $d$; fix a basis $b$, and let $\rho(g)$ be the matrix of $g$ in $b$. Each $\rho(g)$ is invertible, with inverse $\rho(g^{-1})$, since the action is multiplicative and $\rho(1) = 1$. The remaining steps are results proved elsewhere in this development. There is a Breuil-Kisin datum for $K$. There is a period $\tau \in A_{\mathrm{inf}}$ with $\varphi(\tau) = \mathrm{ev}(E)\,\tau$ and $\varphi(\tau) = \eta\,([\varepsilon] - 1)$ for a unit $\eta$ and an element $\varepsilon \in \mathcal{O}_C^\flat$ that corresponds to a compatible system of $\ell$-power roots of unity with $\varepsilon^{(1)} \neq 1$. Since $V$ is crystalline, $\rho$ has a seed of periods on a disc, and the seed has a height datum. From these come a stratified $\varphi$-module $S$ of rank $d$ and a matrix $U$ that realises $S$ for $\rho$. By the main result of the next section, some F-crystal $M$ has a frame by $S$. A frame and a realising matrix give a realisation of $T$ by $M$ at $P_{\mathrm{st}}$. $\square$

The classical reason is this. Over the disc where $[\varpi^\flat]$ is small, the crystalline comparison gives a matrix of periods that is integral up to a bounded denominator. Its Frobenius matrix descends to $\mathfrak{S}$ and gives $A$, and its $G_K$-action gives the stratification $\varepsilon$. The height datum bounds the poles, and $AA' = E^b$ records that the Hodge-Tate weights are bounded.

**Remark 6.13.8 (Formalization).** The statement is the proposition `GlobalTheory.Published.BhattScholzeIntegral` in [BhattScholzeIntegral.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/BhattScholzeIntegral.lean#L12); it lies in the folder `PublishedTheorems`, but [the proof](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BhattScholzeIntegral.lean#L14) proves it. The facts (a), (b) and (c) are `GlobalTheory.T.etaleRealisation_indep_ainfModel`, `GlobalTheory.T.exists_FCrystalHom_of_equivariantEtaleMap_ainf` and `GlobalTheory.T.fCrystalHom_eq_of_etale_realisation_perfectPrism`, second names of `GlobalTheory.Prism.realisation_indep_model`, `GlobalTheory.BSP.exists_fHom_of_equivariant` and `GlobalTheory.BSP.fHom_eq_of_realises`; we read their statements but not their proofs. In the second Theorem, the steps are `GlobalTheory.T.nonempty_breuilKisinDatum`, `GlobalTheory.T.exists_breuilKisin_frobenius_period`, `GlobalTheory.T.exists_crystalline_lattice_periods_on_disc`, `GlobalTheory.T.nonempty_discPeriodAinfBasisData_of_isPer`, `GlobalTheory.T.exists_stratified_phiModule_crystalline_lattice`, `GlobalTheory.T.exists_framed_fCrystal_of_stratifiedPhiModule` and `GlobalTheory.T.etaleRealisation_of_framedMatrices`; the invertibility of $\rho(g)$ is `isUnit_toMatrix_actT`. We did not unfold `Seed`, `Height`, `Lattice`, `LocTied` or `IsCrys`; crystalline means here that $D_{\mathrm{cris}}$ of the period data has $\mathbb{Q}_\ell$-dimension $[K_0 : \mathbb{Q}_\ell] \dim V$, and the paragraph after the proof gives the classical reason, not the Lean proof. The period data enter only through `IsStd P AI`, which is `Nonempty (LocTied l P AI)`. In Part 2 the modules $T$, $T'$ are arbitrary and $\rho$, $\rho'$ are arbitrary maps, not representations; a realisation forces $\rho$ to be multiplicative (`Realises.ρ_mul`). The map $\Phi_{P,d}$ of an F-crystal is given for every $d \in I$, including $d = 0$, where $A[1/d] = 0$ and the condition is empty; the realisation condition 2 asks only for $d \neq 0$. The second name is proved by `first | exact ...` under `maxHeartbeats 1000000`.
