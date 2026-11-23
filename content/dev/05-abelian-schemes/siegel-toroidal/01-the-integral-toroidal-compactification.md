---
title: The integral toroidal compactification
decls:
  - GlobalTheory.siegelToroidalIntegral_holds
  - GlobalTheory.T.siegelToroidalCompactification_polarisedCharts
  - GlobalTheory.SiegJoin.siegelToroidalPolCharts
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The integral toroidal compactification

This section states the main theorem of the chapter. The Siegel moduli scheme of genus $g$ and odd level $n \ge 3$ over $\mathbb{Z}[\zeta_n, 1/n]$ has a smooth projective compactification. On it, the universal abelian scheme extends to a semi-abelian scheme, each point has a chart of a fixed toroidal form, and a twist of a power of the Hodge bundle by the boundary is ample. We prove it from a second form with *polarized* charts, and the second form from five inputs. One input, the charts on a normalized blowup, is the subject of Sections 2 to 7. The theorem is an input to the covolume bound of [the step on characters from the literature](/step/every-character-of-literature/), through [Theorem 1.5.5 of Volume 15](/entry/siegel-toroidal-integral-of-literature/).

**Definition 9.1.1 (The base ring).** Let $n \ge 1$ and let $\zeta_n = e^{2\pi i/n} \in \mathbb{C}$. We write $\Lambda_n = \mathbb{Z}[\zeta_n, 1/n]$ for the subring of $\mathbb{C}$ that $\zeta_n$ and $1/n$ generate. In $\Lambda_n$ the integer $n$ is a unit, and for each ring homomorphism $\beta : \Lambda_n \to K$ to a field, $\beta(\zeta_n)$ is a primitive $n$-th root of unity.

Lean: `GlobalTheory.SiegelTor.cycAway`, `GlobalTheory.SiegelTor.zetaAway`.

**Definition 9.1.2 (Siegel datum).** Let $o$ be a ring, $\zeta \in o$, $h, n \ge 1$, and let $s : S \to \operatorname{Spec} o$ be a scheme over $o$. A *Siegel datum* of genus $h$ and level $n$ on $S$ consists of:

1. an abelian scheme $A \to S$ ([abelian schemes](/learn/abelian-varieties/#abelian-schemes));
2. a line bundle $P$ on $A \times_S A$ that is trivial on $\{0\} \times A$ and on $A \times \{0\}$, with an isomorphism $P \cong \sigma^* P$, where $\sigma$ swaps the factors;
3. an additive map $\ell : \mathbb{Z}^{2h} \to A(S)$ with $n \ell(a) = 0$ for all $a$.

At each geometric point $\bar x$ of $S$ over a map $\beta : o \to k$, the map $\ell$ must induce an isomorphism $(\mathbb{Z}/n)^{2h} \cong A_{\bar x}[n]$, and the Weil pairing of the bundle $P_\Delta = \Delta^* P$ must send $(\ell(a), \ell(b))$ to $\beta(\zeta)^{2\omega(a,b)}$, where $\omega$ is the standard symplectic form on $\mathbb{Z}^{2h}$. The datum is *principal* if $P_\Delta$ is relatively ample and $P$ is nondegenerate: a point $x \in A(T)$ such that $P$ is trivial on $\{x\} \times A_T$ is zero.

Lean: `ReciprocityTheory.ChartRestriction.G.Semi.SiegPre` (also `ReciprocityTheory.ChartRestriction.G.Semi.SiegPre.Principal`).

So $P$ is the Poincaré bundle pulled back by a polarization ([polarizations](/learn/abelian-varieties/#polarizations-and-zarhins-trick)), and $P_\Delta$ is twice the polarization; hence the factor $2$.

**Definition 9.1.3 (Siegel family).** A *Siegel family* of genus $h$ and level $n$ over $(o, \zeta)$ is a scheme $X$ with a map $s : X \to \operatorname{Spec} o$ that is smooth of relative dimension $h(h+1)/2$ and quasi-projective, and a principal Siegel datum $\mathcal{U} = (A, P, \ell)$ on $X$, with two properties ([Siegel moduli schemes](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures)).

1. (Representability.) Let $S$ be a reduced scheme over $o$ whose points over the generic point of $\operatorname{Spec} o$ are dense, and let $c$ be a principal Siegel datum on $S$. Then there is a map $f : S \to X$ over $o$ such that $c$ is the pullback of $\mathcal{U}$ along $f$, compatibly with $P$ and $\ell$.
2. (Injectivity.) Let $R$ be a local ring and $x, y : \operatorname{Spec} R \to X$ with $s \circ x = s \circ y$. If one Siegel datum is the pullback of $\mathcal{U}$ along $x$ and along $y$, then $x = y$.

Lean: `GlobalTheory.ZM.SFam`.

In this chapter, $o = \Lambda_n$ and $\zeta = \zeta_n$, and $\mathcal{U} = (A, P, \ell)$ always denotes the universal datum of the family. The *Hodge bundle* of a smooth group scheme $G \to S$ of relative dimension $g$ is $\omega_G = \det e^* \Omega^1_{G/S}$, a line bundle on $S$.

**Definition 9.1.4 (Polarization function).** An *invariant function* is a rule $\varphi$ that assigns a real number $\varphi(B)$ to each real-valued bilinear form $B$ on $\mathbb{Z}^m$, for each $m$, such that $\varphi(B \circ (r \times r)) = \varphi(B)$ for each surjective linear map $r : \mathbb{Z}^{m'} \to \mathbb{Z}^m$, and $\varphi = 0$ on $\mathbb{Z}^0$. So $\varphi$ is defined on forms on any free module $X$ of finite rank. A *cone* for $\varphi$ is a family $\gamma_1, \dots, \gamma_m$ of symmetric integral bilinear forms on $X$ such that each $\gamma_i$ is positive semidefinite, the family is part of a $\mathbb{Z}$-basis of the symmetric forms, $\varphi$ is linear on the cone it spans, and a strictness condition holds. We say that $\varphi$ is a *polarization function* of rank $q$ if, for each $X$ of rank at most $q$:

1. $\varphi$ is homogeneous of degree $1$ and superadditive on the cone of positive semidefinite real forms;
2. $\varphi(\beta) \in \mathbb{Z}$ for each positive semidefinite integral form $\beta$, and $\varphi(\beta) > 0$ if also $\beta \ne 0$;
3. each subfamily of a cone is a cone;
4. each positive semidefinite real form is a nonnegative real combination of the members of one cone;
5. up to $\operatorname{GL}(X)$, there are finitely many forms that occur in cones.

The function $\varphi$ has *no self-intersections* if, for each cone $\gamma$ on $X$ of rank at most $q$, no automorphism $u$ of $X$ satisfies $u^* \gamma_i = \gamma_j$ with $i \ne j$.

Lean: `GlobalTheory.PolFan.InvFun`, `GlobalTheory.PolFan.IsCone`, `GlobalTheory.PolFan.IsPolFan` (also `GlobalTheory.PolFan.NoSelfInt`).

Properties 3 to 5 say that the cones form a $\operatorname{GL}(X)$-admissible fan, and 1 and 2 that $\varphi$ is a polarization function for it ([toroidal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications)).

**Definition 9.1.5 (Relative parameters).** Let $b : o \to R$ be a map to a local ring $(R, \mathfrak{m})$. Elements $t_1, \dots, t_m \in \mathfrak{m}$ are *relative parameters* for $b$ if, whenever $\sum_i c_i t_i \in \mathfrak{m}^2 + b(b^{-1}\mathfrak{m}) R$, all $c_i$ lie in $\mathfrak{m}$.

Lean: `GlobalTheory.SiegelTor.IsRelParam`.

So the $t_i$ are independent in the relative cotangent space.

**Definition 9.1.6 (Chart).** Fix a Siegel family $F$ of genus $g$ and level $n$ over $\Lambda_n$, a scheme $\bar s : \bar S \to \operatorname{Spec} \Lambda_n$ with an open immersion $j : X \to \bar S$, a group scheme $G$ over $\bar S$ with $e : A \to G$, an invariant function $\varphi$, an effective Cartier divisor $B$ on $\bar S$ and $d \ge 1$. A *chart* at $x \in \bar S$ consists of a regular local ring $R$ with $\xi : \operatorname{Spec} R \to \bar S$ and $t_1, \dots, t_m \in R$, a local domain $R'$ with $\rho : R \to R'$ and $r_i \in R'$, degeneration data $D$ over $R'$ with a uniformization of a group scheme $G'$ over $R'$ and $\pi : G' \to G$, forms $\gamma_i$ on the character group of $D$, and integers $a_i \ge 0$, such that:

1. $R$ is complete, $\xi$ lies over $\Lambda_n$, sends the closed point to $x$, is an étale completion at $x$, and is formally unramified at the residue field;
2. the $t_i$ are relative parameters, the ideal of $\bar S \setminus j(X)$ along $\xi$ is $(t_1 \cdots t_m)$, and $\xi(\mathfrak{p}) \in j(X)$ if and only if $t_1 \cdots t_m \notin \mathfrak{p}$;
3. $R'$ is an admissible base of characteristic $0$, $\rho$ is injective, finite and local, and $r_i^2 = \rho(t_i)$;
4. the uniformization is compatible with $F$, $j$ and $e$ along $\xi \circ \operatorname{Spec} \rho$ (defined below), the rank of the character group is at most $g$, $\gamma$ is a cone for $\varphi$, and the periods of $D$ are the monomials in the $r_i$ with exponents $2n\gamma_i$;
5. $a_i = d \, \varphi(n\gamma_i)$ and the ideal of $B$ along $\xi$ is $(t_1^{a_1} \cdots t_m^{a_m})$.

Lean: `GlobalTheory.SiegelTor.HasChart`.

*Compatible* along $\eta : \operatorname{Spec} R' \to \bar S$ means: $G'$ is the pullback of $G$ along $\eta$ via $\pi$, and there is $y : \operatorname{Spec} K' \to X$, with $K'$ the fraction field of $R'$ and $j \circ y = \eta|_{K'}$, such that the abelian variety of the uniformization is $y^*A$, its Mumford bundle is the pullback of $P$, and the uniformization followed by $e$ is $\pi$ on the generic fibre. Mumford's construction and uniformizations are in [semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction).

**Definition 9.1.7 (Mumford data).** Let $R$ be a domain. *Mumford data* $Q$ over $R$ consist of an abelian scheme $B_Q$ over $R$ of relative dimension $g_Q$, a rigidified, cubical, relatively ample line bundle $M$ on $B_Q$ with trivial $K$-group, a free $\mathbb{Z}$-module $Y$ of finite rank, an additive map $c : Y \to B_Q(R)$, and for $a, b \in Y$ a generator $\tau(a, b)$, over the generic point of $\operatorname{Spec} R$, of the fibre at $(c(a), c(b))$ of the inverse of the Mumford bundle $\Lambda(M) = m^* M \otimes p_1^* M^{-1} \otimes p_2^* M^{-1} \otimes 0^* M$. The $\tau(a, b)$ are symmetric and additive in $a$, up to the cubical structure. We say that $Q$ is *positive* if for each $y \ne 0$, $\tau(y, y)$ is an element of $\mathfrak{m}$ times a generator over $R$, and that $Q$ has *monomial periods* $t^{\delta}$ if $\tau(a, b)$ is $\prod_i t_i^{\delta_i(a,b)}$ times a generator over $R$.

Lean: `GlobalTheory.PolDeg.Data` (also `GlobalTheory.PolDeg.Data.IsPos`, `GlobalTheory.PolDeg.Data.IsMonomialTau`).

**Definition 9.1.8 (Polarized chart).** With $F$, $\bar s$, $j$, $G$, $e$, $\varphi$, $B$ and $d$ as above, a *polarized chart* at $x$ consists of a complete regular local domain $R$ of characteristic $0$ with a map $\xi$ and elements $t_i$ as in conditions 1 and 2 of a chart, Mumford data $Q$ over $R$, forms $\delta_1, \dots, \delta_m$ on $Y$ and integers $a_i$, such that:

1. $Q$ is positive, and for each finite injective map $\rho : R \to R'$ to a complete, integrally closed, noetherian local domain of characteristic $0$ and each degeneration datum $D$ over $R'$ that refines $Q$, there is a uniformization of a group $G'$ over $R'$ with a map $G' \to G$, compatible with $F$, $j$ and $e$ along $\xi \circ \operatorname{Spec}\rho$;
2. the rank of $Y$ is at most $g$, $\delta$ is a cone for $\varphi$, for each $y \ne 0$ some $\delta_i(y,y) > 0$, and $Q$ has monomial periods $t^{n\delta}$;
3. $a_i = d \, \varphi(n\delta_i)$ and the ideal of $B$ along $\xi$ is $(t_1^{a_1} \cdots t_m^{a_m})$.

Lean: `GlobalTheory.PolDeg.HasPolChart` (also `GlobalTheory.PolDeg.IsMumfordOf`).

Refinement is defined in the section on degeneration data along a trait.

**Theorem 9.1.9 (Integral toroidal compactification).** For each $g \ge 1$ there is a polarization function $\varphi$ of rank $g$ such that the following holds for each odd $n \ge 3$. There are a Siegel family $F$ of genus $g$ and level $n$ over $\Lambda_n$ with base $X$, a scheme $\bar s : \bar S \to \operatorname{Spec}\Lambda_n$, an open immersion $j : X \to \bar S$, a group scheme $G$ over $\bar S$ with a map $e : A \to G$, an effective Cartier divisor $B$ on $\bar S$ and integers $d, N$, such that:

1. $\bar s$ is projective and smooth of relative dimension $g(g+1)/2$, and $\bar s \circ j = s$;
2. each $x \in \bar S$ lies in the closure of $j(X) \cap \bar s^{-1}(\bar s(x))$;
3. $G$ is semi-abelian and smooth of relative dimension $g$, $A$ is the pullback of $G$ along $j$ via $e$, and $G$ is abelian exactly over $j(X)$;
4. $d \ge 1$, and there is a chart at each point of $\bar S$;
5. $N \ge 1$, $\omega_G^{N}$ is generated by global sections, and there is $k_0$ such that $\omega_G^{Nk} \otimes \mathcal{O}(-B)$ is ample for all $k \ge k_0$.

Lean: `GlobalTheory.siegelToroidalIntegral_holds`.

This is the toroidal compactification of Faltings and Chai, over $\Lambda_n$ instead of $\mathbb{Z}[1/n]$ (G. Faltings, C.-L. Chai, *Degeneration of Abelian Varieties*, Chapters IV and V).

**Theorem 9.1.10 (Toroidal compactification with polarized charts).** Let $g \ge 1$ and let $\varphi$ be a polarization function of rank $g$ with no self-intersections. Then for each odd $n \ge 3$ there are data as in the theorem above with conditions 1 to 3, $d \ge 1$, a polarized chart at each point, $N \ge 1$, $\omega_G^N$ generated by global sections, and one $k$ such that $\omega_G^{Nk} \otimes \mathcal{O}(-B)$ is ample.

Lean: `GlobalTheory.T.siegelToroidalCompactification_polarisedCharts` (also `GlobalTheory.SiegJoin.siegelToroidalPolCharts`, the proof).

*Proof.* Here $n \ne 0$ and $\Lambda_n$ is noetherian. We use five inputs.

1. There is a Siegel family $F$ of genus $g$ and level $n$ over $\Lambda_n$. We fix one.
2. There is a minimal compactification $z : Z \to \operatorname{Spec}\Lambda_n$ of $X$ with an open immersion $i : X \to Z$ and an ample line bundle $\mathcal{O}_Z(1)$, of the kind in [Theorem 9.19.1](/entry/minimal-siegel-compactification-exists/). It is projective and normal, $i$ has dense image and $z \circ i = s$.
3. By [Theorem 9.18.3](/entry/normalised-blowup-ample-divisor-compactification/), there are $d \ge 1$, an ideal sheaf $J$ on $Z$ whose support misses $i(X)$, and the normalized blowup $\pi : \bar S \to Z$ of $J$, an open immersion $j : X \to \bar S$ with $\pi \circ j = i$, $\pi^{-1}(i(X)) = j(X)$ and dense image, with $z \circ \pi$ projective. The divisor $B = \pi^{-1}J$ has valuation $d\varphi$ along traits, and $\pi^*\mathcal{O}_Z(k) \otimes \mathcal{O}(-B)$ is ample for $k \ge k_0$.
4. By the [theorem on charts](/entry/minimal-blowup-smooth-with-semi-abelian-charts/), $z \circ \pi$ is smooth of relative dimension $g(g+1)/2$ and each point of $\bar S$ has a pre-chart. This step uses that $\varphi$ has no self-intersections.
5. By [Theorem 4.17.9](/entry/semi-abelian-descent-from-complete-regular-charts/), the pre-charts give $G$ and $e : A \to G$ with condition 3.

Set $\bar s = z \circ \pi$. Then $\bar s \circ j = z \circ i = s$. A comparison of Hodge bundles gives $a, N_1 \ge 1$ with $\omega_G^{N_1} \cong \pi^* \mathcal{O}_Z(a)$. Since $\mathcal{O}_Z(1)$ is ample, this and the ampleness in step 3 give $N \ge 1$ with $\omega_G^{N}$ generated by global sections and one $k$ with $\omega_G^{Nk} \otimes \mathcal{O}(-B)$ ample. The pre-chart at $x$ shows that $x$ lies in the closure of $j(X)$ in its fibre, and, together with the properties of $G$ and $n \ne 0$, it gives a polarized chart at $x$. $\square$

*Proof of the integral toroidal compactification.* Fix $g \ge 1$. By [Theorem 7.26.5](/entry/exists-invariant-smooth-proj-fan-no-self-intersections/), there is a polarization function $\varphi$ of rank $g$ with no self-intersections. Let $n \ge 3$ be odd. The theorem with polarized charts gives $F$, $\bar S$, $j$, $G$, $e$, $B$, $d$, $N$ and $k$. Conditions 1 to 3 hold. By a lemma on charts with monomial periods, each polarized chart at $x$ gives a chart at $x$. This step uses $n \ne 0$. For condition 5, let $k' \ge k$. Then
$$\omega_G^{Nk'} \otimes \mathcal{O}(-B) = \omega_G^{N(k'-k)} \otimes \bigl(\omega_G^{Nk} \otimes \mathcal{O}(-B)\bigr)$$
is the tensor product of a line bundle generated by global sections and an ample line bundle, so it is ample ([ample line bundles](/learn/positivity-resolution/#ample-nef-and-big-line-bundles)). So $k_0 = k$ works. $\square$

**Remark 9.1.11 (Formalization).** Two theorems are named `siegelToroidalIntegral_of_polCharts`, in `GlobalTheory` and in `GlobalTheory.PolDeg`, with different statements ([SiegelIntegralToroidalOfPolarisedChartsForFan.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelIntegralToroidalOfPolarisedChartsForFan.lean#L12), [SiegelIntegralToroidalOfPolarisedCharts.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelIntegralToroidalOfPolarisedCharts.lean#L16)). The `T.*` names are wrappers that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. Only odd $n$ occurs. A chart asks for square roots $r_i^2 = \rho(t_i)$ and exponents $2n\gamma_i$; a polarized chart has exponents $n\delta_i$ over $R$ itself. We have not unfolded `Unif`, `IsMonomial`, `IsEtaleCompletion`, `AdmBase`, `IsStrict`, `LinearOn`, `Out.WeilIs` or `LieVB.omega`. The lemmas that turn a polarized chart into a chart, compare Hodge bundles and give the closure of fibres have no entries; we use only their statements.
