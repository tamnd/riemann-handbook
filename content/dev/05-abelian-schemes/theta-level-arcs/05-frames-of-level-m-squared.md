---
title: Frames of level m squared
decls:
  - GlobalTheory.OneBasis.exists_isFrame_pow_sq
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Frames of level m squared

A frame of level $N$ at a point $x$ of a model is a family of sections of $L^N$ over $x$ that becomes a basis of the sections of $L^N$ over every complete trait through $x$. In this section we prove that an arc point with good behaviour at all complete traits, and with a frame of level $1$, has a frame of level $m^2$ for each odd $m$ that is a unit in $O'$, after a finite normal extension of the base. The sections of level $m^2$ come from the theta table of the level $1$ section, and the main work is to correct their valuations at the traits where $X$ is not a unit by a power of $X$. The result is used in [the arc family theorem](/entry/arc-fam/). For sections of line bundles on abelian schemes see [the algebraic theory of theta functions](/learn/theta-functions-cm/#the-algebraic-theory-of-theta-functions) in Volume 1.

### Frames and trait data

We keep the notation of the earlier sections. Let $G \to Y$ be the universal semi-abelian scheme with its line bundle $L$. A *complete trait* is a complete discrete valuation ring of characteristic $0$.

**Definition 6.5.1 (Linear combination along a map).** Let $h : T' \to T$ be a map of $Y$-schemes, let $b_1, \dots, b_n$ be sections of $L^N$ on $G_T$, let $c_1, \dots, c_n$ be functions on $T'$ and let $s$ be a section of $L^N$ on $G_{T'}$. We say that $s = \sum_i c_i\, h^* b_i$ if this holds for the values of the sections on every chart of $G_{T'}$ on which $L$ is trivial.

**Definition 6.5.2 (Basis along a map).** The family $b$ is a *basis along $h$* if each section $s$ of $L^N$ on $G_{T'}$ is $\sum_i c_i\, h^* b_i$ for a unique family $c$.

**Definition 6.5.3 (Frame).** Let $R_1$ be a domain, let $x : \operatorname{Spec} \operatorname{Frac} R_1 \to Y$, and let $b_1, \dots, b_n$ be sections of $L^N$ over $x$. The family $b$ is a *frame of level $N$ at $x$* if the following holds for every complete trait $W$, every map $\varphi : R_1 \to W$ with a compatible map $\gamma$ of fraction fields, and every map $\chi : \operatorname{Spec} W \to Y$ that extends $x \circ \gamma$. There is a basis $b'$ of the sections of $L^N$ over $\chi$ such that, for each $i$, the pullback of $b_i$ along $\gamma$ and the restriction of $b'_i$ to the generic point of $W$ are the same section.

So a frame is a family over the generic point that extends to a basis at every trait.

**Definition 6.5.4 (Arc data at a trait).** Let $W$ be a complete trait, let $f : O' \to W$ and $u \in W$, and let $\chi : \operatorname{Spec} W \to Y$. The point $\chi$ *has the arc data* of $a$ with parameter $u$ if the pullback of $G$ along $\chi$ is a semi-abelian scheme $t$ over $W$ with a uniformisation $P$ at the maximal ideal whose abelian part, line bundle, rigidification, $\mathcal{O}_E$ action and period map are the pullbacks along $f$ of those of $a$, whose $\psi$ is the $\psi$ of $a$ times $u^{\beta_a(y,y)/2}$, and whose level points of level $A$ and $M$ are those of $a$.

**Definition 6.5.5 (Trait data).** Let $(g, y_1)$ be a pair with $g : O'[[X]] \to R_1$ and $y_1$ a point of $X_{o,F}$ over $\operatorname{Frac} R_1$ that lies over $b$. The pair has *trait data* for $a$ if, for every complete trait $W$, every $\varphi : R_1 \to W$ with compatible $\gamma$, and every $\chi : \operatorname{Spec} W \to Y$ that extends $j \circ y_1 \circ \gamma$:

1. if $\varphi(g(X))$ is a unit of $W$, then $\chi$ maps into the abelian locus of $G$;
2. if $\varphi(g(X))$ is not a unit, then there is a finite injective map $W \to W'$ to a complete trait such that $\chi$, pulled back to $W'$, has the arc data of $a$ with parameter the image of $\varphi(g(X))$.

### The theorem

**Theorem 6.5.6 (Frames of level $m^2$).** Assume the seven inputs. Let $Y$ be a model of $X_o$, let $(O', \varpi)$ be an arc base and let $a$ be an arc over $(O', b)$. Let $R_1$ be an integrally closed domain, let $g : O'[[X]] \to R_1$ be injective and finite, and let $y_1$ be a point of $X_{o,F}$ over $\operatorname{Frac} R_1$. Assume that $(g, y_1)$ has trait data for $a$, realises $a$, and has a frame $(\theta)$ of level $1$ at $j \circ y_1$, with one section. Let $m$ be odd and a unit in $O'$. Then there are an integrally closed domain $R_2$, an injective and finite map $h : R_1 \to R_2$ with a compatible map $h'$ of fraction fields, and a frame of level $m^2$ at $j \circ y_1 \circ h'$.

Lean: `GlobalTheory.OneBasis.exists_isFrame_pow_sq`.

*Proof.* If $m = 1$, take $R_2 = R_1$, $h$ the identity, and the frame $(\theta)$. So assume $m \geq 3$. Since $O'$ is a field or a discrete valuation ring, it is local and noetherian, and $R_1$ is noetherian of characteristic $0$, being finite over $O'[[X]]$. Fix an odd prime $n$ that is a unit in $O'$.

*Step 1: a theta basis at the generic point.* The pullback of $G$ to the generic point of $R_1$ is a polarized abelian variety $A$ with a rigidification, since $y_1$ lies in the abelian locus. There is a family $\tau_1, \dots, \tau_r$ of sections of $L^{m^2}$ over $j \circ y_1$ that is a basis after every field extension. Over an algebraic closure $K$ of $\operatorname{Frac} R_1$, the sections $\theta$ and $\tau_i$ give a *theta table*: the values of $\theta$ at the $m^2$-torsion points, and the coefficients of the translates of $\theta^{m^2}$ in the basis $\tau$. Since $m$ and $n$ are odd, this table is complete and single valued at levels $m^2$ and $n$.

*Step 2: the exponent.* The arc $a$ has a positive form $\beta_a$ on its character lattice $\mathsf{X}_0$. There are integers $d \geq 1$ and $C$ such that, for every lattice $\mathsf{X}$ isomorphic to $\mathsf{X}_0$ with a quadratic form $Q = w \cdot \beta_a/2$, and for every adapted family of $r$ shortest representatives of the classes of $\mathsf{X}/m^2 \mathsf{X}$, the sum of $Q$ over the family is $C w m^2 / d$. Put $\kappa = X^C$.

*Step 3: the local matrices.* Let $W$ be a complete trait, with $\varphi : R_1 \to W$ and $\chi$ as in the definition of a frame. We show that, after a finite extension $W \to W'$ of complete traits, there are a basis of the sections of $L^{m^2}$ over $W'$ and a matrix $B$ that expresses $\tau$ in this basis, such that the theta table is *near* to the table of this basis: the entries are controlled by $B$ and by $\kappa$ and $d$. If $\varphi(g(X))$ is a unit, then by the trait data $\chi$ lies in the abelian locus, and the uniformisation of the pullback of $G$ over $W$ has a trivial torus, so the table over $W$ has no correction. If $\varphi(g(X))$ is not a unit, then the trait data give an extension $W'$ where $\chi$ has the arc data of $a$. There the valuation of $\psi(y)$ is $\beta_a(y, y)/2$ times the valuation of $X$. Mumford's theta functions give a basis of $L^{m^2}$ over $W'$, indexed by shortest representatives of the classes, and Step 2 computes the total correction in terms of $\kappa$.

*Step 4: a global matrix.* Let $P$ be the set of valuation rings of $K$ that are centred on such traits. There is $S_0 \in P$, centred on the closed point, such that a function that is integral on all of $P$ and a unit at $S_0$ is a unit on all of $P$. With Step 3 this gives a matrix $\Phi$ over $K$ such that, at each trait, $\Phi$ is a matrix with unit determinant times the local matrix $B$.

*Step 5: descent.* The entries of $\Phi$ are algebraic over $\operatorname{Frac} R_1$. So there is a finite normal extension $R_2$ of $R_1$ whose fraction field contains them. Recombining the basis $\tau$ by $\Phi$ gives sections $f_1, \dots, f_r$ of $L^{m^2}$ over $j \circ y_1 \circ h'$. At each trait the family $f$ is a unit matrix times a basis, so it is a basis over the extension $W'$. A basis over a finite extension $W'$ of a complete trait $W$ that is defined over $W$ is a basis over $W$, by flatness of $G$. So $f$ is a frame of level $m^2$. $\square$

**Remark 6.5.7 (Formalization).** The Lean proof is in [MemRangeIffOfFinite.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/MemRangeIffOfFinite.lean#L163). The hypothesis that $(g, y_1)$ realises $a$ is not used: it is introduced as `_` at line 164, as are four of the seven inputs. The steps use statements of the development that we did not unfold: `exists_thetaBasis_after_every_field_extension`, `thetaTable_algClosed_complete_singleValued`, `shortestRepresentatives_form_sum_depends_on_lattice`, `exists_uniformisation_trivial_torus_abelianLocus`, `arcData_psi_valuation_eq_half_form`, `exists_place_centred_closed_point_detects_units`, `exists_global_matrix_eq_unit_det_mul_local`, `exists_finite_normal_ext_containing_algebraic_elements`, `exists_basis_recombination_invertible_matrix_trait` and `trait_sectionBasis_descends_finite_dvr_extension`. Our proof is a sketch that follows these steps; the exact form of the nearness condition is `Tab.Near`, which we did not unfold. The definition of a frame uses `Lin`, a condition on values in charts with `Good`.
