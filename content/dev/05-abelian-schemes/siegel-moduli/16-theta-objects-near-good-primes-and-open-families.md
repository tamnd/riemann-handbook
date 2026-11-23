---
title: Theta objects near good primes and open families
decls:
  - GlobalTheory.ZM.NearBuild.exists_tObj_near
  - GlobalTheory.T.exists_thetaObject_near_good_prime
  - GlobalTheory.ZM.OpenFamily.nonempty_wFam
  - GlobalTheory.T.nonempty_thetaFamily_over_open_closure
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta objects near good primes and open families

This section builds a universal theta level object over an open part of the scheme of theta values. There are two steps. The first is local: if a family of theta values over a ring $R$ is the family of theta values of a theta level object at one prime $\mathfrak{q}_0$, then, after inverting one element outside $\mathfrak{q}_0$, it is the family of theta values of a theta level object over the localization, and this object receives every geometric object with these theta values. The second step covers the scheme of theta values by such charts and glues the local objects with [the gluing theorem](/entry/theta-affine-glue-exists-glue/). The result is an *open family*, the first approximation to [the theta families](/entry/nonempty-theta-fam/), and it is used in the construction of moduli spaces at levels that are powers of a prime. The background is [theta functions with characteristics](/learn/theta-functions-cm/#theta-functions-with-characteristics) and [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures).

We use the theta level objects and their maps of [the section on theta level objects](/entry/derivation-eq-zero-of-ks-zero/), and the theta values, the coset condition, the theta ideal, the points from a class, the shape and the good classes of [the section on theta families](/entry/nonempty-theta-fam/). Fix $g \ge 0$, a finite set $J$, integer matrices $M_j \in M_{2g}(\mathbb{Z})$ for $j \in J$, an integer $\kappa$ and an odd prime $n$. For $N' \ge 1$ let $I = (\mathbb{Z}/N'^2)^{2g}$ be the set of labels.

**Definition 5.16.1 (Coordinates by sections).** Let $X$ be a scheme with a line bundle $\delta$ and sections $\theta_a$ of $\delta$ for $a \in I$. A point $x : \operatorname{Spec} R \to X$ has *coordinates* $v \in R^I$ if there is a generator $\tau$ of $x^* \delta$ with $x^* \theta_a = v_a \tau$ for every $a$.

Lean: `GlobalTheory.ZM.SecCoord`.

**Definition 5.16.2 (Theta coordinate scheme).** Let $o$ be a ring and $\mathcal{I} \subseteq o[X_a : a \in I]$ an ideal. A *theta coordinate scheme* for $\mathcal{I}$ consists of a scheme $s : Y \to \operatorname{Spec} o$, quasi-projective and [[Flat|5M6KS8F47R]], with $Y$ reduced, and a line bundle $\delta$ on $Y$ with sections $\theta_a$ ($a \in I$), such that:

1. if $x \in Y(R)$ lies over $\beta : o \to R$ and has coordinates $v$, then $v$ is a point of the theta scheme of $\mathcal{I}$ over $\beta$, that is, $F^\beta(v) = 0$ for all $F \in \mathcal{I}$ and $v$ satisfies the coset condition at every prime of $R$;
2. for every ring map $\beta : o \to R$ and every point $v$ of the theta scheme over $\beta$, there is exactly one $x \in Y(R)$ over $\beta$ with coordinates $v$.

Lean: `GlobalTheory.ZM.MMPre`.

So $Y$ is the open part of the projective scheme of $\mathcal{I}$ where the coset condition holds, with $\theta_a$ the coordinate sections.

**Definition 5.16.3 (Object primes).** Let $o$ carry a base $b$ of level $N'^2$, let $\beta : o \to R$ be a ring map and $v \in R^I$. The set of *object primes* of $v$ is the set of ideals $\ker(x)$, for ring maps $x : R \to K$ to [[algebraically closed|0PF6TM8TWT]] fields, such that there is a theta level object over $K$ (over $o$ through $x \circ \beta$) of shape $(M, \kappa)$ with theta values $x(v)$. A set $P$ of ideals of $R$ is *dense* if every element of $R$ that lies in every prime ideal of $P$ is zero.

Lean: `GlobalTheory.ZM.objPrimes`, `GlobalTheory.ZM.DenseP`.

If $R$ is reduced, $P$ is dense if and only if the closure of $P$ in $\operatorname{Spec} R$ is all of $\operatorname{Spec} R$.

**Theorem 5.16.4 (Theta objects near a good prime).** Assume the laws and the second laws of abelian schemes. There is $j_0$ such that the following holds for all $j \ge j_0$, with $N' = n^j$. Let $o$ be a ring with a base $b$ of level $N'^2$, $R$ a [[Noetherian ring|0670T59HGE]] that is reduced, $\beta : o \to R$ a ring map and $v \in R^I$. Assume that the object primes of $v$ are dense. Then for every object prime $\mathfrak{q}_0$ of $v$ there are $f \in R$ with $f \notin \mathfrak{q}_0$ and a theta level object $t$ of level $N'^2$ over $R_f$ such that:

1. $t$ has theta values the images of $v$ in $R_f$;
2. for every algebraically closed field $K$, every ring map $x : R_f \to K$ and every theta level object $t'$ over $K$ of shape $(M, \kappa)$ with theta values $x(v)$, there is a map $t' \to t$ over $\operatorname{Spec} x$.

Lean: `GlobalTheory.ZM.NearBuild.exists_tObj_near` (also `GlobalTheory.T.exists_thetaObject_near_good_prime`, a second name).

*Proof.* Three lemmas, each valid for $j$ above a bound $j_1$, $j_2$ or $j_3$, give the inputs. The first gives embedding data: for every object of level $N'^2$ over an algebraically closed field with theta values $v$, a power of $L$ embeds the abelian variety into projective space, with coordinates $p_c(a)$ that are polynomials in $v$, a fixed Hilbert [[polynomial|0SDC934R52]] and a fixed degree. The second gives the addition morphism of a family near a good prime. The third extends the endomorphisms $\alpha_j$ near a good prime. Take $j_0 = j_1 + j_2 + j_3 + 2$ and $j \ge j_0$.

*The element $f$.* Since $\mathfrak{q}_0$ is an object prime, there are $x : R \to K$ with kernel $\mathfrak{q}_0$ and an object over $K$ with theta values $x(v)$. A lemma on theta values shows that these values satisfy the coset condition at the zero ideal of $K$, so there is $a_0$ with $v_{a_0} \notin \mathfrak{q}_0$. The embedding data show that for each $c$ the coordinates $p_c(a)$ at $x$ generate the unit ideal of $K$, so there is $a_c$ with $p_c(a_c) \notin \mathfrak{q}_0$. Put
$$\begin{aligned} f = v_{a_0} \prod_c p_c(a_c). \end{aligned}$$
Since $\mathfrak{q}_0$ is prime, $f \notin \mathfrak{q}_0$.

*Localization.* The object primes of the images of $v$ in $R_f$ are again dense, and $\mathfrak{q}_0$ corresponds to an object prime $\mathfrak{q}_1$ of $R_f$. A lemma on localizations reduces the claim to the same claim over $R_f$ at $\mathfrak{q}_1$, since a localization of $R_f$ at an element is a localization of $R$. Over $R_f$ the element $v_{a_0}$ and all $p_c(a_c)$ are units.

*The chain.* Over $R_f$ four lemmas apply in turn. Each one inverts one more element outside the prime, and the composite of these localizations is again a localization $R_{f'}$ with $f' \notin \mathfrak{q}_0$.

1. Since the $p_c(a_c)$ are units, the projective coordinates cut out a flat family $Z$ in projective space over the localization, with a line bundle and sections, whose geometric fibres are the abelian varieties of the objects with theta values $v$.
2. The fibre at $\mathfrak{q}_0$ is smooth of dimension $g$, so after a localization $Z$ is [[smooth|EXKGG9X6J0]] of relative dimension $g$.
3. The second input gives an addition morphism on $Z$; after a localization the fibres are geometrically connected, and a lemma on group families with dense good fibres makes $Z$ an abelian scheme.
4. A lemma on polarized families gives a symmetric relatively ample line bundle; after a localization its group $K(L)$ is trivial; the third input extends the endomorphisms.

The result is a theta level object $t$ over $R_{f'}$ with theta values $v$, and the construction is compatible with every geometric object of shape $(M, \kappa)$ with these theta values, which gives the map $t' \to t$. $\square$

**Definition 5.16.5 (Open family).** Let $o$ carry a base $b$ of level $N'^2$, $em : o \to \mathbb{C}$ a ring map and $\mathcal{C}$ a class of complex theta level objects over $em$. An *open family* for $\mathcal{C}$ consists of:

1. a theta coordinate scheme $Y$ for the theta ideal of $\mathcal{C}$;
2. an open set $U \subseteq Y$ and a theta level object $t^u$ over $U$;

such that:

1. the points of $U$ that come from $\mathcal{C}$ are [[Dense|0BSJSX7ME2]] in $U$;
2. for every ring $R$, every $x \in U(R)$ and every $v \in R^I$, the object $t^u$ has theta values $v$ at $x$ if and only if $x$ has coordinates $v$ in $Y$;
3. for every algebraically closed field $K$, every $x \in Y(K)$ and every theta level object $t'$ over $K$ of shape $(M, \kappa)$ with theta values $v$ that are coordinates of $x$, the point $x$ lies in $U$ and there is a map $t' \to t^u$ over $x$.

Lean: `GlobalTheory.ZM.WFam`.

**Theorem 5.16.6 (Open families exist).** Assume the laws and the second laws. Let $w, w' \in J$. There is $j_0$ such that for all $j \ge j_0$, every ring $o$ with a base of level $(n^j)^2$, every arithmetic base $em : o \to \mathbb{C}$ and every class $\mathcal{C}$ of complex theta level objects of level $(n^j)^2$ that is good of some dimension $d$ for $(M, \kappa, w, w')$, there is an open family for $\mathcal{C}$.

Lean: `GlobalTheory.ZM.OpenFamily.nonempty_wFam` (also `GlobalTheory.T.nonempty_thetaFamily_over_open_closure`, a second name).

*Proof.* A lemma on generic objects gives $j_1$, and the previous theorem gives $j_2$. Take $j_0 = \max(j_1, j_2, 2)$ and $j \ge j_0$, and write $N' = n^j$.

*The coordinate scheme.* Since $o$ is a [[Dedekind domain|7NPY2CN5KB]], a lemma on the theta ideal shows that it is radical, homogeneous and torsion free: if $cF$ lies in it with $c \ne 0$ in $o$, then $F$ lies in it. A lemma on coordinate schemes then gives a theta coordinate scheme $Y$ for the theta ideal.

*Generic objects.* The lemma on generic objects shows: for every affine open $x : \operatorname{Spec} R \to Y$ with coordinates $v$ and every minimal prime $\mathfrak{q}$ of $R$, there is a theta level object over an algebraically closed field, at a point with kernel $\mathfrak{q}$, of shape $(M, \kappa)$, with theta values $v$, which comes from $\mathcal{C}$. This is the place where the hypothesis that $\mathcal{C}$ is good enters.

*Charts.* A *chart* is an affine open $x : \operatorname{Spec} R \to Y$ with coordinates $v$ and a theta level object $t$ over $\operatorname{Spec} R$ with theta values $v$ that receives every geometric object of shape $(M, \kappa)$ whose theta values are coordinates of the point. The previous theorem gives charts near every point of $Y$ at which some geometric object of shape $(M, \kappa)$ has the coordinates as theta values. Its density hypothesis holds by the step on generic objects, since $Y$ is reduced.

*Gluing.* Let $U$ be the union of the images of all charts. Two charts agree on their overlaps, since both receive the same geometric objects and maps over a reduced base are unique. The gluing theorem, with $m = n$, gives a theta level object $t^u$ over $U$ with maps from the objects of the charts. Here $n \ge 2$, $n^2 \mid n^j$ since $j \ge 2$, and $n^j$ is odd.

*The conditions.* The points from $\mathcal{C}$ are dense in $U$, by the step on generic objects. The theta values of $t^u$ at $x$ are the coordinates of $x$, since this holds on each chart. Let $x \in Y(K)$ with an object $t'$ of shape $(M, \kappa)$ whose theta values are coordinates of $x$. Then the image of $x$ lies in a chart, so in $U$, and $x$ factors through $U$. The chart receives $t'$, and composing with the map to $t^u$ gives $t' \to t^u$. $\square$

**Remark 5.16.7.** An open family is weaker than a theta family. It has a universal object only over the open set $U$, and it does not claim that $U$ is a fine moduli space or that it is infinitesimally rigid. What it gives is the identification of theta values with coordinates on $U$, and that every geometric object of shape $(M, \kappa)$ is a fibre of $t^u$. The integer $n$ plays two parts: the level is $(n^j)^2$, and $m = n$ is the auxiliary integer of the rigidity statement in the gluing theorem.

**Remark 5.16.8 (Formalization).** In [ExistsThetaObjectNearGoodPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsThetaObjectNearGoodPrime.lean#L176) the bound is $j_1 + j_2 + j_3 + 2$, from `T.exists_goodThetaObjectEmbeddingData`, `T.exists_addition_morphism_thetaFamily_near_goodPrime` and `T.exists_endomorphisms_extend_near_good_prime`. The claim is first turned into `NearC`, and the chain is `nearC_of_den_loc`, `nearC_of_unimodular`, `nearC_of_fam`, `nearC_of_smooth` and `nearC_of_grpFam`, which call lemmas such as `NearCut.exists_away_flat_projRep`, `NearBuild.grpFam_of_dense_fibres` and `NearBuild.kTriv_near_good_prime`. In [NonemptyThetaFamilyOverOpenClosure.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/NonemptyThetaFamilyOverOpenClosure.lean#L527) the bound is `max (max j₁ j₂) 2`, the coordinate scheme comes from `T.nonempty_thetaCoordinateSchemeData` and `ThIdeal.thIdeal_radical_homogeneous_torsionFree`, the generic objects from `T.exists_generic_object_minimalPrime_moduli_chart`, and the open set from `exists_covered` (line 466), which calls the gluing theorem at line 510 with $m = n$. The step that the image of a geometric point lies in $U$ uses `first | exact Subsingleton.elim q pt | ...` for the one point of $\operatorname{Spec} K$. We followed the statements of the helper lemmas and did not open the proofs of all of them, so the description of the chain is a reading of their statements. The hypotheses `n.Prime` and `Odd n` are both assumed; `Odd n` only excludes $n = 2$. The second names are wrappers proved by `first | exact @...` under `maxHeartbeats 1000000`.
