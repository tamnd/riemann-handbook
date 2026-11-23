---
title: Charts on the normalized blowup
decls:
  - GlobalTheory.T.minimalBlowup_smooth_with_semiAbelianCharts
  - GlobalTheory.SiegJoin.chartSt5_holds
  - GlobalTheory.T.exists_tautological_chart_at_siegel_blowup_point
  - GlobalTheory.TChart.exists_chart_at
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Charts on the normalized blowup

The toroidal compactification is built as a normalized blowup $S$ of a minimal compactification $Z$ of the Siegel family. This section proves that $S$ is smooth over $\Lambda_n$ of relative dimension $g(g+1)/2$ and that each point of $S$ has a pre-chart: a complete local ring with parameters $t_i$ that cut out the boundary, Mumford data with monomial periods, and a semi-abelian group that is abelian exactly off the boundary. The main input is a tautological chart at each point, built from a trait through the point and the [degeneration data along a trait](/entry/exists-deg-from-of-trait/). The pre-charts give the polarized charts of the [integral toroidal compactification](/entry/siegel-toroidal-integral-holds/).

Fix $g \ge 1$, an odd $n \ge 3$, and a Siegel family $F$ of genus $g$ and level $n$ over $\Lambda_n$, with base $s : X \to \operatorname{Spec}\Lambda_n$ and universal datum $(A, P, \ell)$. For a domain $R$ we write $\iota_R : \operatorname{Spec} K_R \to \operatorname{Spec} R$ for the generic point.

**Definition 9.7.1 (Minimal compactification data).** Let $z : Z \to \operatorname{Spec}\Lambda_n$, let $i : X \to Z$ and let $\mathcal{O}_Z(1)$ be a line bundle on $Z$. These are *minimal compactification data* for $F$ if:

1. $(Z, z, i)$ is a theta compactification of $F$ (in particular $i$ is an open immersion), $z$ is projective, $Z$ is normal and noetherian, $z \circ i = s$, $i$ has dense image, and $\mathcal{O}_Z(1)$ is ample;
2. there are a ring $o'$ with a finite injective map $\beta : \Lambda_n \to o'$, a normal scheme $S'$ projective over $o'$, a dense open $U \subseteq S'$, a finite surjective map $c : U \to X$ and a proper surjective map $\pi' : S' \to Z$ with $\pi'|_U = i \circ c$ and $z \circ \pi'$ equal to $S' \to \operatorname{Spec} o' \to \operatorname{Spec} \Lambda_n$;
3. there is a commutative semi-abelian group scheme $G$ over $S'$, smooth of relative dimension $g$, whose restriction to $U$ is the group pullback of $A$ along $c$;
4. there is $N \ge 1$ with $\pi'^* \mathcal{O}_Z(1) \cong \omega_G^{\otimes N}$, where $\omega_G$ is the Hodge bundle of $G$.

Lean: `GlobalTheory.SiegJoin.MinAt5`.

The model is the minimal compactification of Faltings and Chai, where $\mathcal{O}_Z(1)$ is a power of the Hodge bundle ([toroidal and minimal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications)).

**Definition 9.7.2 (Normalized blowup).** Let $\varphi$ be an invariant function and $d \ge 0$. Let $j : X \to S$ and let $J$ be an ideal sheaf on $S$. Then $J$ has *valuation $d\varphi$ along traits* if for each trait $\mathcal{T}$ for $F$, with ring $V$, uniformizer $\varpi$, map $y$ and form $\beta$, and each $\xi : \operatorname{Spec} V \to S$ with $\xi \circ \iota_V = j \circ y$, there is an integer $a \ge 0$ with $a = d\,\varphi(\beta)$ and $J$ generates the ideal $(\varpi^a)$ of $V$ along $\xi$. A map $\pi : S \to Z$ is a *normalized blowup* of an ideal sheaf $J$ on $Z$ if $S$ is normal and $\pi = \pi_0 \circ \nu$ for a blowup $\pi_0 : S_0 \to Z$ of $J$ and a finite $\nu$ that is an isomorphism over a dense open $U \subseteq S_0$ with dense inverse image.

Let $(Z, z, i)$ be as above, let $\pi : S \to Z$, $j : X \to S$, and let $B$ be an effective Cartier divisor on $S$. These are *blowup data* of order $d$ for $\varphi$ if there is an ideal sheaf $J$ on $Z$ such that $d \ge 1$, the support of $J$ does not meet $i(X)$, $J$ has valuation $d\varphi$ along traits through $i$, $\pi$ is a normalized blowup of $J$, $z \circ \pi$ is projective, $j$ has dense image, $\pi \circ j = i$, $\pi^{-1}(i(X)) = j(X)$, the ideal sheaf of $B$ is $\pi^{-1} J \cdot \mathcal{O}_S$, and the ideal sheaf of $B$ has valuation $d\varphi$ along traits through $j$.

Lean: `GlobalTheory.SiegJoin.BlowAt` (also `GlobalTheory.Poinc.ValOn`, `GlobalTheory.Poinc.IsNormBl`).

**Definition 9.7.3 (Mumford family).** Let $R$ be a local domain, $y : \operatorname{Spec} K_R \to X$, $G_1$ a group scheme over $R$, $\alpha_1$ a map from its generic fibre to $A$, and $Q$ Mumford data over $R$. Then $(G_1, y, \alpha_1)$ is a *Mumford family* for $Q$ if $R$ is a CN domain, $Q$ is positive, and for each local CN domain $R'$ with an injective finite map $\rho : R \to R'$, and each degeneration data $D$ over $R'$ with respect to $\mathfrak{m}_{R'}$ that refine $Q$ along $\rho$ and some $Y_D \cong Y_Q$, there are a group scheme $G'$ over $R'$, $\pi : G' \to G_1$, a polarized abelian scheme $A'$ over $K_{R'}$ and a uniformization of $G'$ by $D$ and $A'$ along $\rho$, with respect to $y$, $G_1$ and $\alpha_1$.

Lean: `GlobalTheory.PolDeg.IsMumfordFam`.

**Definition 9.7.4 (Pre-chart).** Let $s_S : S \to \operatorname{Spec} o$, let $j : X \to S$ be an open immersion, let $\varphi$ be an invariant function, $B$ an effective Cartier divisor on $S$, $d \ge 0$ and $x \in S$. A *pre-chart* at $x$ consists of a regular local domain $R$, maps $b : o \to R$ and $\xi : \operatorname{Spec} R \to S$, elements $t_1, \dots, t_m \in R$, Mumford data $Q$ over $R$, forms $\delta_i$ on $Y_Q$, integers $a_i \ge 0$, and $G_1$, $y$, $\alpha_1$ as above, such that:

1. $R$ is complete of characteristic $0$, $s_S \circ \xi = \operatorname{Spec} b$, $\xi$ sends the closed point to $x$, the map $\mathcal{O}_{S,x} \to R$ is an étale completion, and $\mathcal{O}_{S,x} \to R \to k_R$ is formally unramified;
2. the $t_i$ are relative parameters for $b$, the ideal sheaf of the complement of $j(X)$ generates $(\prod_i t_i)$ along $\xi$, and $\xi(\mathfrak{p}) \in j(X)$ if and only if $\prod_i t_i \notin \mathfrak{p}$;
3. $G_1$ is semi-abelian, its abelian locus is the set of $\mathfrak{p}$ with $\prod_i t_i \notin \mathfrak{p}$, $j \circ y = \xi \circ \iota_R$, and $\alpha_1$ makes the generic fibre of $G_1$ the group pullback of $A$ along $y$;
4. $(G_1, y, \alpha_1)$ is a Mumford family for $Q$, $Y_Q$ has rank at most $g$, the $\delta_i$ are a cone for $\varphi$, for each $z \ne 0$ some $\delta_i(z, z) > 0$, and $Q$ has monomial periods $t^{n\delta}$;
5. $a_i = d\,\varphi(n\delta_i)$ for each $i$, and the ideal sheaf of $B$ generates $(\prod_i t_i^{a_i})$ along $\xi$.

Lean: `GlobalTheory.PolDeg.PreChart` (also `GlobalTheory.PolDeg.IsGenFibre`).

**Definition 9.7.5 (Tautological chart).** A *tautological chart* of genus $g$ and level $n$ for $\varphi$ consists of:

1. a lower base $L$ of level $n$ with Siegel family of genus $h$, ring $W$ and tautological base $T$ of rank $r$, with $h + r = g$;
2. integers $m, N$ and a basis $\varepsilon_1, \dots, \varepsilon_{m+N}$ of the symmetric bilinear forms on $\mathbb{Z}^r$, such that $\varepsilon_1, \dots, \varepsilon_m$ is a cone for $\varphi$ and for each $x \ne 0$ some $\varepsilon_k(x, x) > 0$ with $k \le m$;
3. a local domain $R$ and a map $\psi : W[x_1, \dots, x_{m+N}] \to R$ that *completes at a prime*: $R$ is noetherian and complete, $\psi$ is flat, $\mathfrak{m}_R$ is generated by $\psi(\psi^{-1}\mathfrak{m}_R)$, and each $r \in R$ has $a, b$ with $\psi(b)$ a unit and $r\psi(b) - \psi(a) \in \mathfrak{m}_R$;
4. $\psi|_W$ is local, $t_k = \psi(x_k) \in \mathfrak{m}_R$ for $k \le m$, and $\psi(x_{m+k})$ is a unit for each $k$;
5. Mumford data $Q$ over $R$ with $e : Y_Q \cong \mathbb{Z}^r$ that come from $T$ via $(\psi|_W, \psi(x), \varepsilon, n)$.

Let $b_C : \Lambda_n \to R$ be the composite of $b_T$ and $\psi|_W$. The chart is a *family* for $F$ with $(G_1, y, \alpha_1)$ if $G_1$ is semi-abelian, its abelian locus is the set of $\mathfrak{p}$ with $\prod_{k \le m} t_k \notin \mathfrak{p}$, $\alpha_1$ makes the generic fibre of $G_1$ the group pullback of $A$ along $y$, $(G_1, y, \alpha_1)$ is a Mumford family for $Q$, and $s \circ y = \operatorname{Spec} b_C \circ \iota_R$.

Lean: `GlobalTheory.TChart.Taut` (also `GlobalTheory.TChart.IsComplAt`, `GlobalTheory.TChart.Taut.IsFam`).

**Theorem 9.7.6 (Charts on the normalized blowup).** Let $\varphi$ be a polarization function of rank $g$ with no self-intersections. Let $(Z, z, i, \mathcal{O}_Z(1))$ be minimal compactification data for $F$, and let $(\pi : S \to Z, j, B)$ be blowup data of order $d$ for $\varphi$, with $j$ an open immersion. Then $z \circ \pi$ is smooth of relative dimension $g(g+1)/2$, and $S$ has a pre-chart at each point $x$, for $z \circ \pi$, $j$, $\varphi$, $B$ and $d$.

Lean: `GlobalTheory.SiegJoin.chartSt5_holds` (also `GlobalTheory.T.minimalBlowup_smooth_with_semiAbelianCharts`, a wrapper; the statement is `GlobalTheory.SiegJoin.ChartSt5`).

*Proof.* The two claims are two lemmas with the same hypotheses: one gives the smoothness of $z \circ \pi$, the other gives a pre-chart at each $x$. Both apply the next theorem at the given point. $\square$

This is the toroidal compactification of Faltings and Chai, *Degeneration of Abelian Varieties*, Springer 1990, Chapter IV, Section 6, and Chapter V, Section 5, as a normalized blowup of the minimal one.

**Theorem 9.7.7 (Tautological chart at a point).** With the hypotheses of the theorem above, for each $x \in S$ there are a tautological chart $C$ of genus $g$ and level $n$ for $\varphi$, with ring $R$, a group scheme $G_1$ over $R$, maps $y : \operatorname{Spec} K_R \to X$ and $\alpha_1$, and $\xi : \operatorname{Spec} R \to S$, such that $C$ is a family for $F$ with $(G_1, y, \alpha_1)$, $j \circ y = \xi \circ \iota_R$, and $\xi$ sends the closed point of $\operatorname{Spec} R$ to $x$.

Lean: `GlobalTheory.TChart.exists_chart_at` (also `GlobalTheory.T.exists_tautological_chart_at_siegel_blowup_point`, a wrapper).

*Proof.* Step 1 (the scheme $S$). The map $z \circ \pi$ is projective and $\Lambda_n$ is a finitely generated ring, so $S$ is separated and locally noetherian, and $z \circ \pi$ is locally of finite type. Also $j$ has dense image and $z \circ \pi \circ j = z \circ i = s$.

Step 2 (a trait through $x$). A lemma on traits gives a trait $\mathcal{T}$ for $F$, with ring $V$ and map $y_{\mathcal{T}}$, a map $\xi_{\mathcal{T}} : \operatorname{Spec} V \to S$ and $b : \Lambda_n \to V$, such that $\xi_{\mathcal{T}}$ sends the closed point to $x$, $\xi_{\mathcal{T}} \circ \iota_V = j \circ y_{\mathcal{T}}$ and $z \circ \pi \circ \xi_{\mathcal{T}} = \operatorname{Spec} b$. So $s \circ y_{\mathcal{T}} = \operatorname{Spec} b \circ \iota_V$.

Step 3 (degeneration data). The theorem on degeneration data along a trait gives a lower base $L$ with ring $W$ and tautological base $T$ of rank $r$, a basis $\varepsilon$ indexed by $m + N$, a CN domain $V'$ with $f : V \to V'$ injective and local, a local map $\kappa : W \to V'$ with $\kappa \circ b_T = f \circ b$, elements $s_k \in V'$, degeneration data $D'$ over $V'$ with $e : Y' \cong \mathbb{Z}^r$ that come from $T$ via $(\kappa, s, \varepsilon, n)$, and a uniformization $U'$ along $f$ of a group $G'$ over $V'$.

Step 4 (the chart). The ring $W$ is regular: it is an étale completion of a local ring of the $r$-fold fibre power of the family of $L$, which is regular. Let $\psi_V : W[x] \to V'$ be $\kappa$ on $W$ and $x_k \mapsto s_k$. A lemma on completions over a regular local ring gives a local domain $R$, a map $\psi : W[x] \to R$ that completes at a prime with $\psi|_W$ local, and a local map $\theta : R \to V'$ with $\theta \circ \psi = \psi_V$. As $\theta(\psi(x_k)) = s_k \ne 0$, $\psi(x_k) \ne 0$. A lemma on data from a tautological base gives Mumford data $Q$ over $R$ with $e_Q$ that come from $T$ via $(\psi|_W, \psi(x), \varepsilon, n)$. For $k \le m$, $\psi(x_k) \in \mathfrak{m}_R$, as else $s_k$ would be a unit. For $k > m$, $s_k$ is a unit and $\theta$ is local, so $\psi(x_k)$ is a unit. This gives a tautological chart $C$ with ring $R$, and $\theta \circ b_C = \kappa \circ b_T$.

Step 5 (the Mumford family). A lemma gives a commutative group scheme $G_1$ over $R$ with a bundle $P_1$ on $G_1 \times G_1$, such that $(Q, G_1, P_1)$ is a Mumford polarization, $P_1$ is canonical over the open set where $t = \prod_{k \le m} t_k$ is a unit, $G_1$ is abelian exactly where $t$ is a unit, and the $n$-torsion of $G_1$ over algebraically closed fields comes from $K_R$. As $\theta(t) = \prod_k s_k \ne 0$, also $t \ne 0$, and the map $R \to V' \to K_{V'}$ extends to $\kappa' : R[1/t] \to K_{V'}$.

Step 6 (the generic fibres). Let $f_K : K_V \to K_{V'}$ extend $f$. By a lemma on generic fibres, which uses Step 4 and $U'$, $(A, P)$ pulled back along $y_{\mathcal{T}} \circ \operatorname{Spec} f_K$ and $(G_1, P_1)$ pulled back along $\operatorname{Spec}\kappa'$ have a common group pullback with isomorphic bundles. From Steps 2 to 4, $s \circ y_{\mathcal{T}} \circ \operatorname{Spec} f_K = \operatorname{Spec}(\kappa' \circ b_C)$.

Step 7 (level structure). A lemma gives a principal Siegel datum $c$ of genus $g$ and level $n$ over $R[1/t]$, isomorphic to the restriction of $(G_1, P_1)$. Each $y_U : \operatorname{Spec} R[1/t] \to X$ over $b_C$ that pulls the universal datum back to $c$ has $y_U \circ \operatorname{Spec}\kappa' = y_{\mathcal{T}} \circ \operatorname{Spec} f_K$. A second lemma gives $y$, $\alpha_1$, such a $y_U$, and the inclusion $l : R[1/t] \to K_R$, such that $C$ is a family for $F$ with $(G_1, y, \alpha_1)$ and $y = y_U \circ \operatorname{Spec} l$.

Step 8 (extension). A lemma on extension to the normalized blowup, which uses that $\varphi$ has no self-intersections, gives $\xi : \operatorname{Spec} R \to S$ with $j \circ y = \xi \circ \iota_R$.

Step 9 (the closed point). Since $R$ is a domain and $t \ne 0$, $\operatorname{Spec} l$ is dominant. So two maps from $\operatorname{Spec} R[1/t]$ to a separated scheme that agree after $\operatorname{Spec} l$ are equal. So $s \circ y_U = \operatorname{Spec} b_C$, and $\xi$ restricted to $\operatorname{Spec} R[1/t]$ is $j \circ y_U$. Then
$$\xi \circ \operatorname{Spec}\theta \circ \iota_{V'} = j \circ y_U \circ \operatorname{Spec}\kappa' = j \circ y_{\mathcal{T}} \circ \operatorname{Spec} f_K = \xi_{\mathcal{T}} \circ \operatorname{Spec} f \circ \iota_{V'}.$$
As $\iota_{V'}$ is dominant and $S$ is separated, $\xi \circ \operatorname{Spec}\theta = \xi_{\mathcal{T}} \circ \operatorname{Spec} f$. The maps $\theta$ and $f$ are local, so they send closed points to closed points, and $\xi$ sends the closed point of $\operatorname{Spec} R$ to $\xi_{\mathcal{T}}(\mathfrak{m}_V) = x$. $\square$

**Remark 9.7.8 (Formalization).** The minimal compactification data `MinAt5` are weaker than `MinAt`: they omit the conditions that $\pi'^{-1}(i(X)) = U$, that the abelian locus of $G$ is $U$, the clause on the bundle of $G$, and `SameAbPart` ([MinSt5OfMinSt4.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/MinSt5OfMinSt4.lean#L19), [ExistsMinAt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsMinAt.lean#L20)). In `ChartHit.setup` the properness of $z \circ \pi$ is proved as `hP` and then not used ([ExistsTautologicalChartAtSiegelBlowupPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTautologicalChartAtSiegelBlowupPoint.lean#L33)). The proof of `exists_chart_at` does not name the hypotheses `hdvr` and `hff` (that $V'$ is a discrete valuation ring and that $f$ is finite) which it gets in Step 3 ([ExistsTautologicalChartAtSiegelBlowupPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTautologicalChartAtSiegelBlowupPoint.lean#L133)). The wrappers use `first | exact @X | ...` under `maxHeartbeats 1000000` ([ExistsTautologicalChartAtSiegelBlowupPointStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTautologicalChartAtSiegelBlowupPointStatement.lean#L12)). We have not unfolded `IsThetaCompact`, `hodge`, `IsMumPol`, `Mum.CanonOn` or `TorsRat`. The lemmas cited in the two proofs have no entries in this part; we use only their statements.
