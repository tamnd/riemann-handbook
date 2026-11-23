---
title: Statements for families
decls:
  - Formalism.L2.DIV.LvlWire.slope_lemma_division_side
  - Formalism.L2.DIV.LvlWire.hh_of_lvl
  - Formalism.L2.linkEtaTw_closed
  - Formalism.L2.linkEta_closed
  - Formalism.L2.SG.ThmSOwn.theoremS_transport_link_zero
  - Formalism.L2.DIV.Arith4S.arithClause_rec
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Statements for families

The proof does not use the results of this chapter for one datum at a time. It uses them for families of data indexed by a real parameter $x$, in the sense of Section 7, and it needs them in the form in which they enter [the remaining division bounds on the working class](/entry/b-rest-all-alt/) and [the connectedness statement from Green](/entry/shape-closed-link-n-of-green/). This section collects six such statements. The first two are slope statements: a two-sided comparison of slopes for the division lattice, and a bound for a frame number built from it. The other four sit next to them in the proof but are not about slopes: a dimension count for twisted local systems, a transport statement for the link estimates, and the bookkeeping of the arithmetic clause. We state them because the proof calls them at the same place, and we say plainly what each one is.

### Families and their size data

We keep the definition of Section 7. A family $\mathcal{F}$ with exponent $\varepsilon > 0$ has a starting point $x_1$, for each $x$ a set of indices $i$, and for each pair a datum $D(x, i)$ of the proof. Each datum comes with *size data* $L(x, i)$: the scale $x$ itself, a number $b > 0$, a rank $m$, and further real quantities that measure the datum, among them numbers written $\mathrm{Ga}$, $\mathrm{Fo}$, $B_0$, and for each word $u$ a number $\mathrm{Ee}(u)$ and a level $T_u$. We do not unfold these quantities; the statements below use them only as they appear. A property of data holds *eventually on the family* if there is an $x_0$ such that it holds for $D(x, i)$ for all $x \geq x_0$ and all $i$. Some of the statements below also require $x > x_1$ and some do not; we follow the source in each case.

Each datum carries *division data*. These attach to each word $u$ a hermitian lattice $N_u$, the *division lattice* at $u$, and they carry one more hermitian lattice $R$. We also use the level-zero lattice $A_0(u)$ of Section 4 at the word $u$. All slopes are in the normalization of Section 1, so $\mu$ is the slope and $\mu_{\max}$ the maximal slope.

### The slope lemma for the division lattice

The slope lemma compares the division lattice with the level-zero lattice in both directions, up to an explicit loss. For a constant $C$ and a word $u$, write
$$
\mathrm{Lo}(u) = C\, I + C\, n_T\, m \Big( \frac{a}{k} + b' \Big) \log T_u + C\, X'' + 1 ,
$$
where $I$, $n_T$, $a$, $k$, $b'$ and $X''$ are further size quantities of the datum. Say that the *slope comparison with constant $C$* holds at a datum if, whenever the standing definitions of the datum are in force, for every word $u$ both inequalities
$$
\mu_{\max}(N_u) \leq \mu_{\max}(A_0(u)) + \mathrm{Ga} + \mathrm{Fo} - \mathrm{Ee}(u) + C\, m\, B_0
$$
and
$$
\mu(A_0(u)) + \mathrm{Ga} + \mathrm{Fo} - \mathrm{Ee}(u) - \mathrm{Lo}(u) \leq \mu(N_u)
$$
hold. The first inequality bounds the maximal slope of the division lattice from above by the maximal slope of the level-zero lattice, and the second bounds its slope from below by the slope of the level-zero lattice. The shift $\mathrm{Ga} + \mathrm{Fo} - \mathrm{Ee}(u)$ is the same on both sides, so the two lattices have the same slopes up to $C m B_0$ above and $\mathrm{Lo}(u)$ below.

The hypotheses are five properties of the family. We name them and do not unfold them.

- The *level lines*: eventually on the family, the conditions on the product of the first and zeroth parts hold and the congruence lattices have bounded length.
- The *size of $T_u$*: eventually, $T_u$ is large and $\log T_u \leq C_T\, m\, \Lambda$ for a constant $C_T$ and a size quantity $\Lambda$ of the datum.
- *Positive rank*: eventually, every division lattice $N_u$ is nonzero.
- The *link estimates* $\mathrm{LinkG}$ and $\mathrm{LinkMu}$: there are constants for which the two link inequalities hold eventually, the first with an error $\delta$ that tends to $0$.

**Theorem 1.8.1 (Slope lemma for the division lattice).** Assume that the family has its level lines, the size bound for $T_u$, positive rank and the two link estimates. Then there are $C$ and $x_0$ such that the slope comparison with constant $C$ holds at $D(x, i)$ for all $x \geq x_0$ and all $i$.

Lean: `Formalism.L2.DIV.LvlWire.slope_lemma_division_side`

*Proof.* The level lines give the conclusion of the lemma on the minimal places and the commensurability of the division lattices. Together with the size bound for $T_u$, positive rank and the two link estimates, they give the place conditions for the family: constants $C \geq 0$ and $x_0$ with the local conditions at every datum beyond $x_0$. From these, the slope comparison at each datum follows from the local slope estimate at that datum. The resulting statement holds for every word $u$ without the standing definitions, so it holds in particular when they are in force. $\square$

### The frame number bound

The second statement bounds a *frame number*. At a datum, let $s$ be the explicit frame size of the division lattices $N_u$, a number built from the lattices $N_u$ and an explicit height bound of the datum with a size constant $C_{\mathrm{sz}}$. We use $s$ only through the statement. The *frame number bound with exponent $C_H$* at a datum is
$$
s + \mu_{\max}(R) \leq x^{C_H}\, b ,
$$
and the bound holds *for the family* if there is an $x_0$ such that it holds at $D(x, i)$ for all $x \geq x_0$ with $x > x_1$ and all $i$.

**Theorem 1.8.2 (Frame number bound).** Let $E_b$ and $C_{F}$ be functions of the output constants of the family, and let $C_H$ be such that the family is large for the threshold built from $E_b$, $C_F$ and the hook constant, and for $C_H$. Assume the hypotheses of the slope lemma, and that the family has the complement-two property. Assume also that eventually, for $x > x_1$, every $i$ and every word $u$,
$$
\mu_{\max}(A_0(u)) \leq x^{E_b}\, b ,
$$
and that eventually, for $x > x_1$ and every $i$,
$$
\mu_{\max}(R) + \operatorname{mean}_e \log \kappa_R(e) \leq x^{C_F}\, b ,
$$
where $\kappa_R(e)$ are the positive numbers attached to $R$ by the data and the mean is over the index $e$. Then the frame number bound with exponent $C_H$ and size constant $C_{\mathrm{sz}}$ of the family holds for the family.

Lean: `Formalism.L2.DIV.LvlWire.hh_of_lvl`

*Proof.* The general height bound from component bounds reduces the frame number bound to the following inputs: the slope comparison, positive rank, the fullness of the division lattices, a bound for the gauge form, the size bound for $T_u$, and the two bounds assumed for $A_0(u)$ and $R$. The slope comparison is the slope lemma above. Fullness follows from the level lines through the commensurability of the division lattices. The bound for the gauge form follows from the complement-two property. $\square$

So the bound for the maximal slope of the level-zero lattice proved in Section 7 enters the proof here: through the first inequality of the slope lemma, a bound for $\mu_{\max}(A_0(u))$ of the form $x^{E_b} b$ controls the maximal slope of the division lattice.

### Local systems cover the twists

The next two statements are dimension counts. At a datum, write $\mu_0$ for the base weight and $\mu_w$ for the weight at a place $w$. For each $j$ with $1 \leq j \leq m$ and each $w$ the datum has a finite set $\mathrm{locs}(j, w)$ of local indices, and for each local index $i$ a finitely generated module $M_i$ over a ring $O_i$. Say that the *local systems cover the twists* at the datum if for every $j$ with $1 \leq j \leq m$ and every place $w$ with $\mu_w \neq \mu_0$,
$$
\sum_{i \in \mathrm{locs}(j, w)} \operatorname{rank}_{O_i} M_i = \dim M(\mu_w, j),
$$
where $M(\mu_w, j)$ is the space of the twist by $\mu_w$ in degree $j$.

**Theorem 1.8.3 (Local systems cover the twists).** Suppose that eventually on the family every datum has a family of local modules with a normalized local compatibility for which the Hecke data are tied. Then eventually on the family the local systems cover the twists.

Lean: `Formalism.L2.linkEtaTw_closed`

*Proof.* This is the general covering result for tied Hecke data, applied with the standard Hecke data. $\square$

**Corollary 1.8.4 (The eta link).** Under the same hypothesis, the family has the eta link.

Lean: `Formalism.L2.linkEta_closed`

*Proof.* The eta link of a family is, by definition, the statement that eventually the local systems cover the twists. $\square$

### Transport of the link estimates

The link estimate $\mathrm{LinkS}$ with constant $C_0$ says that eventually on the family, for every $i$, there are $\eta_0, \eta_1$ and $e_0 \geq 0$ with $\eta_0, \eta_1, \sqrt{e_0} \leq \exp(-x^{\varepsilon/8})$ for which a local link inequality holds at $D(x, i)$. A property $P$ of families is *closed* on a class $\mathcal{C}$ of families if there is $\varepsilon_1 > 0$ such that for every $\varepsilon \in (0, \varepsilon_1]$ there is a threshold with this property: every family in $\mathcal{C}$ with exponent $\varepsilon$ that is large for the threshold has $P$.

**Theorem 1.8.5 (Transport of the link estimate).** Let $\mathcal{C}$ be a class of families, $C_0 \geq 1$, and assume the hypotheses of the selected form of Theorem S on $\mathcal{C}$: a selection of row data for each family in $\mathcal{C}$ with the decay of its gaps, finite-dimensional rows, tied local data and tied instances; closed statements for the residual estimate, the selected Theorem S and the point count; the row inequality for the loop; and the positivity of types, rows and main rows. Then the following property is closed on $\mathcal{C}$: if the family satisfies the size bound for $T_u$, then it has the link estimate $\mathrm{LinkS}$ with constant $C_0$.

Lean: `Formalism.L2.SG.ThmSOwn.theoremS_transport_link_zero`

*Proof.* The selected data give the concrete estimate of the selected Theorem S at every datum, and the selection gives the row ties. The general form of the link theorem then combines these with the closed estimates for the off-diagonal and diagonal kernels, whose positivity comes from the positivity of types and rows. $\square$

### The arithmetic clause

The last statement fixes explicit constants. For real numbers $C_h, C_c, C_{YL}, C_t$ put
$$
c_0 = \max\big( 28,\ 2(1 + |C_c|) + 1,\ 1,\ C_h (3 + 2 C_{YL} + \max(C_t, 5) + 3) \big),
$$
and let $c_e$ and $x_0$ be the explicit maxima built from $c_0$ and the constants of the datum, as in the source. The *arithmetic clause* at a word $u$ is a statement about the lattices of an indefinite package, a list of numbers attached to $u$, and an integer $d$; we do not unfold it.

**Proposition 1.8.6 (Arithmetic clause).** Let a datum carry its sizes, a choice of parameters, a finite group $G$ of the given order with subgroups and characters as in the source, and a size bound for the gamma lattices. Let $C, C_h \geq 0$ and $x \geq x_0$. Then for every package there are a real number $\lambda_0 = \log |G|$, two further constants, numerical facts at every word, and an integer $d > 0$ divisible by every gamma index, such that the arithmetic clause holds at every word.

Lean: `Formalism.L2.DIV.Arith4S.arithClause_rec`

*Proof.* The explicit maxima give each needed inequality between the constants and $x$; for instance $c_0 \geq 28$, $x \geq 3 + |C_c|$ and $x \geq 272 + 2 c_e$. With these, the numerical facts and the arithmetic clause follow from the general recursive forms of these statements. The integer $d$ is an explicit positive integer built from the package data and the subgroup, and general lemmas show that it is positive and divisible by every gamma index. $\square$

**Remark 1.8.7 (Formalization).** The slope lemma obtains constants with $0 \leq C$ from the place conditions and drops this sign condition, and its proof never uses the standing definitions of the datum, which are carried as a hypothesis in the statement ([LvlWire.lean](lean:Formalism/LocalToGlobal/Divisibility/DivisibilityRemainder/NoColumnCase/LvlWire.lean#L39)). The slope comparison is defined in [LocalQuadraticParts.lean](lean:Formalism/SharpRestriction/Divisibility/LocalQuadraticParts.lean#L677) and the frame number bound at [line 363](lean:Formalism/SharpRestriction/Divisibility/LocalQuadraticParts.lean#L363) of the same file. The corollary on the eta link only restates the theorem on twists, since the eta link is defined as that statement ([EtaClosed.lean](lean:Formalism/LocalToGlobal/NormalizedHeckeFactors/EtaClosed.lean#L14)). The transport theorem carries an instance assumption on weighted coefficients that its statement does not mention ([LinkSPos.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/LinkSPos.lean#L129)). The arithmetic clause consists of comparisons of explicit thresholds and has no slope content ([ArithClauseRec.lean](lean:Formalism/LocalToGlobal/Divisibility/ArithClauseRec.lean#L22)). We did not unfold the size quantities, the link inequalities, the hypotheses of the transport theorem or the arithmetic clause; the statements above follow their names and the shape of the formal statements.

## Notes and references

Hermitian lattices over the ring of integers of a number field and their degrees and slopes are the hermitian vector bundles over $\operatorname{Spec} \mathcal{O}_K$ of Arakelov geometry. Our account follows Bost's Bourbaki report [Bost, *Périodes et isogénies des variétés abéliennes sur les corps de nombres (d'après D. Masser et G. Wüstholz)*, Séminaire Bourbaki, Exp. 795, Astérisque 237 (1996), §§4 and 5], where the slope, the maximal slope and the slope inequality for a map of bounded norm are set out in the form used in Sections 1 and 7. The norm of a fractional ideal, used in the definition of the degree, is in [Neukirch, *Algebraic Number Theory*, Grundlehren 322, Springer (1999), Chapter I, §5]. The existence of short vectors in the dual lattice, used in Section 7, rests on the transference theorem of Banaszczyk [W. Banaszczyk, *New bounds in some transference theorems in the geometry of numbers*, Math. Ann. 296 (1993), Theorem 2.1]. The factor two between our slope and the slope of Volume 1 comes from the normalization of the realization, as explained in the comparison remark of Section 1.

The statements of this section are used in [the remaining division bounds on the working class](/entry/b-rest-all-alt/) and in [the connectedness statement from Green](/entry/shape-closed-link-n-of-green/), which serve the step [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/) of [the theta matching](/proof/theta-matching/).
