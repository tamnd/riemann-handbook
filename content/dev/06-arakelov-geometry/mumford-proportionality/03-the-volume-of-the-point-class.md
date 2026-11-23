---
title: The volume of the point class
decls:
  - GlobalTheory.BaseVolume.mass_openPart_eq_covol
  - GlobalTheory.T.hodgeMetric_pointClassForm_mass_eq_covolume
  - GlobalTheory.UnifDens.chernTopPart_image
  - GlobalTheory.T.chernTopPart_hodgeMetric_uniformisation_image
  - GlobalTheory.UnifDens.chernTop_domain
  - GlobalTheory.T.pointClassDensity_hodgeMetric_boundedDomain
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The volume of the point class

By [pointwise proportionality](/entry/pointwise-hodge/), all top Chern forms of the Hodge metric that enter the main theorem are multiples of one form: the form of the point polynomial $P_0$. This section computes its total mass on the open part of a Lie base. The answer is the covolume of the arithmetic group. The proof pulls the form back to the bounded symmetric domain, where it is an invariant volume form, and integrates over a fundamental domain. The result is used in [the Chern integrals of the Hodge metric](/entry/has-chern-integral-point-poly-covol/).

We keep the notation of [the previous section](/entry/pointwise-hodge/): a Lie base $X$ of a toroidal flag component $Y_k$, its open part $O$, its framed family $\mathcal{E}$ and the Hodge metric $h$.

**Definition 7.3.1 (Chern measures).** Let $h$ be a Hermitian metric on a framed family $\mathcal{E}$ over $X$ and $R \in \mathbb{R}[c_{\tau,k}]$. For each point $y$ choose one frame $A_y \in S(y)$. The *Chern measures* $\mu_R^+$ and $\mu_R^-$ are the measures on $X(\mathbb{C})$ that, in each algebraic chart $\phi$ of dimension $n = \dim X$, have the densities
$$\max\bigl(\pm\rho_R(G_y)(\phi(y)),\, 0\bigr), \qquad G_y(w) = h_{A_y}(\phi^{-1}(w)),$$
with respect to the pullback of Lebesgue measure on $\mathbb{C}^n$. The measures of the charts are glued to one measure on $X(\mathbb{C})$.

The density does not depend on the chart, up to the Jacobian factor $|\det|^2$, and does not depend on the frame by rule 3 of a Hermitian metric. So $\mu_R^+ - \mu_R^-$ is the [measure](/learn/analysis/#measures-and-integrals) of the form $R(c(h))$, on the set where both are finite.

**Definition 7.3.2 (Bounded domain).** Let $\mathcal{D} = \mathcal{D}_{p,q}^{\Psi}$ be the set of families $z = (z_\tau)_{\tau \in \Psi}$ of complex $p \times q$ matrices with $1 - z_\tau^* z_\tau$ positive definite for each $\tau$. We view $\mathcal{D}$ as an open subset of $\mathbb{C}^{\Psi \times p \times q}$. Let $\mu_{\mathcal{D}}$ be the measure on $\mathcal{D}$ with density
$$\prod_{\tau \in \Psi} \bigl(\operatorname{Re} \det(1 - z_\tau^* z_\tau)\bigr)^{-N}$$
with respect to Lebesgue measure. A *fundamental domain* for a group $\Gamma$ of matrices acting on $\mathcal{D}$ by $z \mapsto (az + b)(cz + d)^{-1}$ is a measurable set $F \subseteq \mathcal{D}$ that meets every orbit, such that the set of $z \in F$ with a translate $\gamma z \neq z$ in $F$ has $\mu_{\mathcal{D}}$-measure $0$.

The domain $\mathcal{D}$ is the product of the bounded realizations of the symmetric spaces of $\mathrm{U}(p, q)$, and $\mu_{\mathcal{D}}$ is its invariant measure: the determinant $\det(1 - z^* z)$ picks up the factor $|\det(cz + d)|^{-2}$ under the group, and the Jacobian of the fractional linear map is $|\det(cz + d)|^{-2N}$.

**Definition 7.3.3 (Constants and covolume).** Put
$$c_{\mathrm{Fl}}(r) = \prod_{i=0}^{r-1} \frac{i!}{\pi^i}, \qquad c_{\mathrm{Gr}}(p, q) = \pi^{-pq} \prod_{i=0}^{p-1} \frac{(q+i)!}{i!}.$$
Then $c_{\mathrm{Fl}}(p+q) = c_{\mathrm{Gr}}(p,q)\, c_{\mathrm{Fl}}(p)\, c_{\mathrm{Fl}}(q)$. The *covolume* of the component $U_k$ of the uniformization is $\operatorname{covol}(U_k) = c_{\mathrm{Fl}}(N)^{|\Psi|}\, \mu_{\mathrm{Fr}}(F)$, where $\mu_{\mathrm{Fr}}$ is the invariant measure on a space of frames of the Hermitian space and $F$ is a fundamental set of the arithmetic group there. It does not depend on the choice of $F$, and it is positive.

We will also use the following form of the covolume: for a fundamental domain $F$ of $\Gamma_k$ in $\mathcal{D}$, we have $\operatorname{covol}(U_k) = c_{\mathrm{Gr}}(p, q)^{|\Psi|}\, \mu_{\mathcal{D}}(F)$.

**Proposition 7.3.4 (Density on the domain).** Let $X, j, f, \mathcal{E}, A_0$ be a Lie base. Let $\psi \colon \mathbb{C}^{\Psi \times p \times q} \to X(\mathbb{C})$ be a map such that, for each point $x$ of the domain of the uniformization $U_k$, the point $j(\psi(x))$ is the image of $x$ under $U_k$. Let $v \in \mathcal{D}$ and $A \in S(\psi(v))$. Then
$$\rho_{P_0}(h_A \circ \psi)(v) = c_{\mathrm{Gr}}(p, q)^{|\Psi|} \prod_{\tau \in \Psi} \bigl(\operatorname{Re} \det(1 - v_\tau^* v_\tau)\bigr)^{-N}.$$

Lean: `GlobalTheory.UnifDens.chernTop_domain` (also `GlobalTheory.T.pointClassDensity_hodgeMetric_boundedDomain`, a second name).

*Proof.* The pullback of the Hodge metric by $\psi$ is the model metric of $\mathcal{D}$, built from the matrices $1 - v_\tau v_\tau^*$ (inverted and transposed) and $1 - v_\tau^* v_\tau$. The top Chern density of $P_0$ for the model metric is invariant under the group of $\mathcal{D}$, which acts transitively. So its value at $v$ is its value at the origin times the factor of the invariant measure, $\prod_\tau (\operatorname{Re} \det(1 - v_\tau^* v_\tau))^{-N}$. At the origin the curvature has constant coefficients, and the top density of $P_0 = \prod_\tau ((-1)^p c_{\tau,p})^q$ is a sum over permutations that gives $c_{\mathrm{Gr}}(p, q)$ for each $\tau$. $\square$

**Proposition 7.3.5 (Mass of an image).** In the setting of the last proposition, let $A \subseteq \mathcal{D}$ be measurable with $\psi$ injective on $A$. Then
$$\mu_{P_0}^+\bigl(\psi(A)\bigr) = c_{\mathrm{Gr}}(p, q)^{|\Psi|}\, \mu_{\mathcal{D}}(A).$$

Lean: `GlobalTheory.UnifDens.chernTopPart_image` (also `GlobalTheory.T.chernTopPart_hodgeMetric_uniformisation_image`, a second name).

*Proof.* First, $\dim X = |\Psi|\,pq$, so $\psi$ goes between spaces of the same dimension. The map $\psi$ is continuous on $\mathcal{D}$ and holomorphic in algebraic charts. Cover $\psi(A)$ by algebraic charts $\phi$. On each piece, the change of variables formula for the holomorphic map $\phi \circ \psi$, injective on $A$, with real Jacobian $|\det_{\mathbb{C}} d(\phi \circ \psi)|^2$, turns the density of $\mu_{P_0}^+$ in the chart into the density $\rho_{P_0}(h \circ \psi)$ on $\mathcal{D}$. By the [density on the domain](/entry/chern-top-domain/) this density is positive, so $\max(\rho, 0) = \rho$, and it equals $c_{\mathrm{Gr}}(p, q)^{|\Psi|}$ times the density of $\mu_{\mathcal{D}}$. The pieces glue, since both sides are measures and agree on a cover. $\square$

**Theorem 7.3.6 (Mass of the point class).** Let $X, j, f, \mathcal{E}, A_0$ be a Lie base for $Y_k$, with open part $O$ and Hodge metric $h$. Then
$$\mu_{P_0}^+\bigl(O(\mathbb{C})\bigr) = \operatorname{covol}(U_k).$$

Lean: `GlobalTheory.BaseVolume.mass_openPart_eq_covol` (also `GlobalTheory.T.hodgeMetric_pointClassForm_mass_eq_covolume`, a second name).

*Proof.* The uniformization of the component gives a map $\psi$ as above with $\psi(\mathcal{D}) = O(\mathbb{C})$. Its fibres are the orbits of the arithmetic group $\Gamma_k$, and $\psi$ is $\Gamma_k$-invariant. Take a fundamental domain $F$ of $\Gamma_k$ in $\mathcal{D}$. Let $F_0 \subseteq F$ be the set of points that have a translate $\gamma z \neq z$ in $F$, and let $F_1 \supseteq F_0$ be a measurable null hull. Then $\psi$ is injective on $F \setminus F_1$: two points of $F$ with the same image are in one orbit, and off $F_0$ they are equal. Since $\psi$ meets $O(\mathbb{C})$ on every orbit, $O(\mathbb{C})$ is $\psi(F \setminus F_1)$ together with $\psi(F_1)$, and $\psi(F_1)$ is $\mu_{P_0}^+$-null, because $\psi$ maps null sets to null sets in charts. The [mass of an image](/entry/chern-top-part-image/) gives
$$\mu_{P_0}^+\bigl(O(\mathbb{C})\bigr) = c_{\mathrm{Gr}}(p, q)^{|\Psi|}\, \mu_{\mathcal{D}}(F \setminus F_1) = c_{\mathrm{Gr}}(p, q)^{|\Psi|}\, \mu_{\mathcal{D}}(F) = \operatorname{covol}(U_k),$$
by the second form of the covolume. $\square$

**Remark 7.3.7.** This is the volume part of Mumford's proof: the top Chern form of the point class of the compact dual, for the invariant metric, is an invariant volume form, so its integral over the quotient is the covolume (Mumford, Invent. Math. 42 (1977), 239 to 272). Here the normalizations $c_{\mathrm{Fl}}$ and $c_{\mathrm{Gr}}$ fix the covolume so that the constant in the main theorem is $1$.

**Remark 7.3.8 (Formalization).** The Chern measures are `chernTopPart` in [InterPolyProdSum.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/InterPolyProdSum.lean#L130). They use one chosen frame at each point (line 132) and the positive part through `ENNReal.ofReal`. The domain and $\mu_{\mathcal{D}}$ are `DomFlat` and `muD` in [Statement.lean](lean:Formalism/DegreeFormula/Statement.lean#L250), with $q$ written as $(p+q) - p$. The covolume is `covol` in [FirstIndexEqOfUnfolded.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/FirstIndexEqOfUnfolded.lean#L89); we did not unfold the measure on frames or the fundamental set. The second form of the covolume is the lemma `covol_eq_muD`, and the fundamental domain comes from `BoundedFundDomain.exists_isFD`; we did not open their proofs. The proof of the theorem uses the condition `IsUnf` to get $p_0 = q$ for the component. The value of the model density at the origin, and its invariance, are lemmas whose proofs we did not open.
