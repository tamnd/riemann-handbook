---
title: The canonical bundle of a toroidal component
decls:
  - GlobalTheory.LogKSDiv.exists_logKS_div
  - GlobalTheory.T.exists_logKodairaSpencer_divisor_toroidalComponent
  - GlobalTheory.LogCanon.exists_kap_theta
  - GlobalTheory.T.exists_toroidalCanonicalBundle_weight_line
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The canonical bundle of a toroidal component

On a toroidal compactification of a Shimura variety, the logarithmic Kodaira-Spencer isomorphism identifies the canonical bundle twisted by the boundary with an automorphic line bundle of a fixed weight. This section proves the form of this fact that the separation of orbits needs. There is a line bundle $\kappa$ on the compactified component whose pullback to the flag cover is the automorphic bundle of the canonical weight, and a section of $\kappa \otimes K^{-1}$ that vanishes exactly on the boundary. The result is used in [the separation of orbits by cusp forms](/entry/separate-orbits-by-cusp/) ([Shimura varieties and toroidal compactifications](/learn/geometry/#shimura-varieties-and-toroidal-compactifications)).

We work with the moduli data of the earlier chapters. Let $E$ be a CM field with host data $H$, $\mathcal{D}$ a datum of signature $(p, q)$ and dimension $\dim \mathcal{D}$, a level, a moduli space with coefficients in a field $F$, a toroidal flag datum and a component $Z$. Write $X_0$ for the toroidal compactification of the component, $s_0 : X_0 \to \mathrm{Spec}\,F$ for its structure map and $j_0 : X_0^\circ \to X_0$ for the open immersion of the interior. The compactified family over $X_0$ is a semiabelian scheme with an action of $E$. For each embedding $\tau : E \to \mathbb{C}$ its Lie algebra has an eigenpart of rank $m_\tau$, the multiplicity of $\tau$ in $\mathcal{D}$. We do not unfold these objects. We assume that $p + q \ge 1$ and that the function field of the moduli space satisfies the closure condition of the earlier chapters.

**Definition 3.14.1 (Eigenframes and canonical weights).** Let $x \in X_0$ and let $\varphi : F \to \mathcal{O}_{X_0, x}$ be the structure map. An *eigenframe* at $x$ is, for each $\tau$, a family of $m_\tau$ elements of the $\tau$-eigenpart of the Lie algebra of the family over the local ring at $x$, that is, a frame of each eigenpart. A *generic eigenframe* $f_0$ is an eigenframe at the generic point. For an eigenframe $f$ at $x$ and the generic eigenframe $f_0$, the *frame change* at $\tau$ is the matrix $A_\tau$ over the function field with $f_{0,\tau,i} = \sum_k (A_\tau)_{i k} f_{\tau,k}$, and $d_\tau = \det A_\tau$. The *canonical weight* of $\tau$ is
$$w(\tau) = \begin{cases} q & \text{if } \tau(\varrho) = \varrho_0, \\ p & \text{otherwise}, \end{cases}$$
where $\varrho \in E$ and $\varrho_0 \in \mathbb{C}$ are the fixed root of the host data and its fixed value.

For a line bundle $K$ with local frames, a Cartier divisor $D'$ *presents* $K$ by rational functions $r_i$ if $r_i$ is a local equation of $D'$ on the $i$-th chart and the frames of $K$ change by the ratios of the $r_i$. So $\mathcal{O}(D') \cong K$.

**Theorem 3.14.2 (Logarithmic Kodaira-Spencer divisor).** Assume $p + q \ge 1$ and the closure condition. Assume that $X_0$ is integral and smooth over $F$ of dimension $\dim\mathcal{D}$. Let $K$ be a canonical bundle of $X_0$, presented by a Cartier divisor $D'$. Let $f_0$ be a generic eigenframe. Let $D$ be a Cartier divisor on $X_0$ such that for every $x \in X_0$ there is an eigenframe $f$ at $x$ with frame changes $A_\tau$, $d_\tau = \det A_\tau$, and
$$\prod_\tau d_\tau^{-w(\tau)} \ \text{is a local equation of } D \text{ at } x.$$
Then there is $h$ in the function field of $X_0$ such that for every $x \in X_0$ there are local equations $g$ of $D$ and $g'$ of $D'$ at $x$ with:

1. $h g / g'$ is regular at $x$;
2. $h g / g'$ is a unit at $x$ if and only if $x$ lies in the interior $X_0^\circ$.

Lean: `GlobalTheory.LogKSDiv.exists_logKS_div` (also `GlobalTheory.T.exists_logKodairaSpencer_divisor_toroidalComponent`, a second name).

In terms of divisors, the conclusion says that $\mathrm{div}(h) + D - D'$ is effective and that its support is the boundary $X_0 \setminus X_0^\circ$. Since $D'$ presents $K$, the canonical bundle is $\mathcal{O}(D)$ twisted by an effective divisor with support on the boundary.

*Proof.* We use two inputs on the logarithmic Kodaira-Spencer map, proved in the development.

*At the generic point.* The logarithmic Kodaira-Spencer isomorphism, applied to the generic eigenframe $f_0$, gives a top form $D_0$ that pairs with top forms of $X_0$ over the function field. Choose a chart $i_0$ of $K$ that contains the generic point, with frame $\omega_{i_0}$. Put
$$h = r_{i_0} \cdot \langle D_0, \omega_{i_0} \rangle.$$
The value does not depend on the chart: for another chart $i$ that contains the generic point, the ratio of $\omega_{i_0}$ and $\omega_i$ is the ratio of $r_i$ and $r_{i_0}$, since $D'$ presents $K$. So $h = r_i \langle D_0, \omega_i \rangle$.

*At a point $x$.* Take the eigenframe $f$ at $x$ and the frame changes $A_\tau$ of the hypothesis. The logarithmic Kodaira-Spencer isomorphism at $x$, applied to $f$, gives a local top form $D_x$. A lemma on frame changes says that the wedge of the Kodaira-Spencer classes changes by the determinants of the frame change, raised to the canonical weights:
$$\langle D_0, \omega \rangle = u \prod_\tau d_\tau^{w(\tau)} \langle D_x, \omega \rangle$$
with $u = \pm 1$. Choose a chart $i$ of $K$ at $x$. With $g = \prod_\tau d_\tau^{-w(\tau)}$ and $g' = r_i$ we get
$$\frac{h g}{g'} = \frac{r_i \langle D_0, \omega_i\rangle\, g}{r_i} = u\, \langle D_x, \omega_i \rangle.$$
The local Kodaira-Spencer input says that $\langle D_x, \omega_i \rangle$ is regular at $x$, and that it is a unit at $x$ exactly when $x$ is in the interior. This gives both conclusions. $\square$

**Theorem 3.14.3 (Canonical bundle and the weight line).** Assume $p + q \ge 1$ and the closure condition, and assume that $X_0$ is smooth over $F$ of dimension $\dim\mathcal{D}$. Let $K$ be a canonical bundle of $X_0$. Then there are a line bundle $\kappa$ on $X_0$ and a section $\theta$ of $\kappa \otimes K^{-1}$ with:

1. $\pi_0^*[\kappa] = [L_0(\kappa_{\mathrm{can}})]$ in the Picard group of the flag cover, where $\pi_0$ is the projection from the flag cover to $X_0$ and $L_0(\kappa_{\mathrm{can}})$ is the automorphic line bundle of the canonical weight;
2. the locus where $\theta$ does not vanish is the interior $X_0^\circ$.

Lean: `GlobalTheory.LogCanon.exists_kap_theta` (also `GlobalTheory.T.exists_toroidalCanonicalBundle_weight_line`, a second name).

*Proof.* By an input lemma, $X_0$ is integral. An input lemma on determinants of Lie eigenparts gives a generic eigenframe $f_0$ and, for every choice of integer weights $a(\tau)$, a Cartier divisor $D$ with local equations $\prod_\tau d_\tau^{-a(\tau)}$ as in the previous theorem, such that $\pi_0^*[\mathcal{O}(D)]$ is the class of the automorphic bundle of the weight defined by $a$. We take $a = w$. The weight defined by $w$ is the canonical weight $\kappa_{\mathrm{can}}$, by a direct comparison of exponents. Put $\kappa = \mathcal{O}(D)$; this gives part 1.

For part 2, choose a chart of $K$ at the generic point. It gives a Cartier divisor $D'$ that presents $K$. The previous theorem gives $h$. A lemma on Cartier divisors turns $h$ into a section $\theta$ of $\mathcal{O}(D) \otimes \mathcal{O}(D')^{-1} = \kappa \otimes K^{-1}$: locally $\theta$ is $h g / g'$. By the previous theorem $\theta$ is regular everywhere and is a unit exactly on the interior. $\square$

**Remark 3.14.4 (Formalization).** The integrality of $X_0$ is a hypothesis of the first theorem but is proved in the second one. The canonical bundle in the second theorem is used only through one chart at the generic point ([ExistsToroidalCanonicalBundleWeightLine.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsToroidalCanonicalBundleWeightLine.lean#L45)). The sign $u$ of the frame change is a unit, so it does not change regularity or the unit condition ([ExistsLogKodairaSpencerDivisorToroidalComponent.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLogKodairaSpencerDivisorToroidalComponent.lean#L25)). We have not unfolded the eigenframes, the Kodaira-Spencer inputs, the closure condition or the automorphic bundle $L_0$. The second names are wrappers.
