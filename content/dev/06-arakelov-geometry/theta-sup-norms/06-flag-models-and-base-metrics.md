---
title: Flag models and base metrics
decls:
  - GlobalTheory.CompanionTheory.Ar.PB.FMX.flagModelExists
  - GlobalTheory.T.flag_model_exists_of_given
  - GlobalTheory.CompanionTheory.Ar.PB.BMx.baseMetricExists_of_given
  - GlobalTheory.T.base_metric_exists_of_given
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Flag models and base metrics

This section builds the two objects on which the square systems of the later sections live. The first is a flag model of a Hodge component: an arithmetic variety in a product of projective spaces whose points are a base point together with flags in the Hodge bundles, cut out by minors of a generic block diagonal matrix. The second is a base metric on a flag model: a resolution of the base with a boundary section, finitely many frames of the Hodge bundles, and their Gram matrices with bounds near the boundary. The two theorems are two of the three parts of the tie statement, which [the root model with a Hodge tie](/entry/tie-of/) proves from five statements and which leads to [square systems on a flag cover](/entry/t-c-sqsys/). For the geometry we use [line bundles and divisors](/learn/geometry/#line-bundles-and-divisors), [hermitian line bundles](/learn/arakelov/#hermitian-line-bundles) and [resolution of singularities](/learn/positivity-resolution/#resolution-of-singularities-and-principalization).

### Hodge components and flag models

Let $E$ be a CM field with a host, let $\Psi$ be the CM type, and let $(p, q)$ be the signature of a hermitian datum, with $N = p + q$. A Hodge component $\mathfrak{M}$ over a point $x_0$ is a component of a model of the unitary Shimura variety of this datum, embedded by coordinates $x_0$ in a product of projective spaces over a field $\Omega$ of characteristic $0$. For each $\tau \in \Psi$ it carries a Hodge bundle $W_\tau$ of rank $p$ and the dual $\Omega_\tau$ of a bundle of rank $q$. A component is a cover of degree $d$ if its map to the moduli space has degree $d$, and it has a normal crossings boundary of dimension $n$ if its coordinates give a model with a simple normal crossings boundary ideal of dimension $n$ whose points are the points outside the interior.

**Definition 10.6.1.** A flag model of type $(N, j)$ over a family of coordinates $y$ with values in a field $\Phi$ consists of:

1. a field $\Omega$ of characteristic $0$ inside $\Phi$ and base coordinates $x$ with values in $\Omega$, which are the base part of $y$;
2. for each $\tau \in \Psi$ a matrix $g_\tau$ over $\Phi$ that is block diagonal for the split $N = (N - j) + j$, such that the entries of the lower unipotent part of $g_\tau B_\tau$ are algebraically independent over $\Omega$ for some block triangular $B_\tau$;
3. a block $k$ of coordinates for every proper step $(\tau, i)$, where a step is proper if $i + 1 \neq j$ and $i + 1 \neq N$; on this block, $y$ is a linear combination with coefficients in $\Omega$ of the minors of $g_\tau$ in the step columns of $i$;
4. degrees $b$ and numbers $\lambda_{\tau,i}$, and for every relevant prime that contains the ideal of $x$ a frame: block diagonal invertible matrices $T_\tau$ over $\Omega$ that transform the coefficients of the minors by monomials in $x$.

So a point of a flag model is a base point $x$ together with, for each $\tau$, the partial flag of the column spans of $g_\tau$. A flag tie of a flag model $M$ to a Hodge component $\mathfrak{M}$ over $M.x$ is a pair of bases $e_W$, $e_\Omega$ of the generic fibres of $W_\tau$ and $\Omega_\tau$ such that the columns of the blocks of $T_\tau$ applied to them are frames of the Hodge bundles at every point where the frame is good.

### The flag model of a Hodge component

The given statements are the standing hypotheses of the development, collected in one proposition.

**Theorem 10.6.2 (Flag model of a Hodge component).** Assume the given statements. Let $\mathfrak{M}$ be a Hodge component over $x_0$ with bases of its Hodge bundles, let $n$ and $d$ be natural numbers, and assume that $x_0$ is an arithmetic variety of dimension $n + 1$ and that $\mathfrak{M}$ is a cover of degree $d$. Then there are a flag model $M$ of type $(p + q, p)$ over coordinates $y$, a Hodge component $\mathfrak{M}_1$ over $M.x$ with a flag tie, a Hodge component $\mathfrak{M}'$ over $y$ with a flag $F$, degrees $x_{\deg}$ and numbers $e$ such that:

1. $\mathfrak{M}_1$ is isomorphic to $\mathfrak{M}$ over a bijective map of fields, by a block map of coordinates that sends $x_0$ to $M.x$, compatibly with the Hodge bundles and the given bases;
2. $\mathfrak{M}_1$ is a cover of degree $d$, $M.x$ is an arithmetic variety of dimension $n + 1$, and a normal crossings boundary of $\mathfrak{M}$ of any dimension is one of $\mathfrak{M}_1$;
3. $y$ is an arithmetic variety of dimension
$$
n + \lvert\Psi\rvert \Bigl(\tbinom{p}{2} + \tbinom{q}{2}\Bigr) + 1 ;
$$
4. the tie is total for $\mathfrak{M}'$, $F$, $x_{\deg}$ and $e$: $\mathfrak{M}'$ is the pullback of $\mathfrak{M}_1$, the vectors of $F$ are the column frames of the blocks of $g_\tau$ applied to the tie bases, the lines of $F$ have root data $x_{\deg}$ and $e$, the degrees of the model are
$$
d_y(\tau, i) = -\sum_{k \leq i} x_{\deg}(\tau, k),
$$
and a product identity between $e$, the determinant factors of $g_\tau$ and the numbers $\lambda$ holds;
5. the flag $F$ has degree $d$.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.FMX.flagModelExists` (also `GlobalTheory.T.flag_model_exists_of_given`, a second name).

*Proof.* The proof does not use the given statements.

Step 1: frames from twisted generators. Each Hodge bundle of $\mathfrak{M}$ is a vector bundle of the expected rank, and the given bases are linearly independent and span its generic fibre. For each bundle there are twisted generators: finitely many sections of twists of the bundle that generate it. They give a matrix $a$, and the frame property gives a left inverse $B$ with $B a = 1$.

Step 2: the model. Put the frame change of $a$ into block form. Its determinant is a monomial times a unit, its minors at proper steps are injective on block diagonal matrices, and the base part of the new coordinates is $x_0$. This gives a flag model $M$ with $g_\tau$ the generic matrix of the frame change and with $y$ the sum of minors of $g_\tau$; the frame change is regular, so the frame data of the definition exist. The field of $y$ is a field of rational functions over $\Omega$ in the entries of the generic matrix.

Step 3: the dimension. The coordinates of the base are an arithmetic variety, and the minors of a generic matrix add one free parameter for each entry of its lower unipotent part. For $\tau$ this is $\binom{p}{2} + \binom{q}{2}$, which gives part 3.

Step 4: the flag. The valuations of the minors of the frame give the leading terms of the frame along every boundary component. From these the proof builds the base change $\mathfrak{M}'$ to $y$, the flag $F$ with its degree $d$, and the degrees $x_{\deg}$. The determinant factor of the generic matrix is $1$, which gives the product identity. $\square$

### Base metrics

**Definition 10.6.3.** Let $M$ be a flag model and $n$ a natural number. A base metric of dimension $n$ on $M$ consists of:

1. a log resolution $\pi : X_b \to \operatorname{Spec}$ of the coordinate ideal of $M.x$, of dimension $n$, with a line bundle $L$ and a section $s$ with simple normal crossings and $\lVert s\rVert \leq 1$, an atlas adapted to $s$, and the boundary $\partial = \{ s = 0 \}$;
2. a finite open cover $O_1, \dots, O_q$ of $X_b$ and frames $F_i$ of $M$ that are good on $O_i$;
3. for each $i$ and $\tau$ a smooth matrix function $G_{i,\tau}$ on $O_i \setminus \partial$ that is block diagonal and positive definite, with entries and inverse entries bounded by a power of the log distance $r_W$ to $\partial$ and with a gradient bound;
4. period maps that realize $G_{i,\tau}$ as Gram matrices of holomorphic periods, and a point where the period map is an immersion;
5. for every step $(\tau, i)$ a hermitian line $h_{\tau,i}$ of degree $d_y(\tau, i)$, with the metrics induced from $G$.

A base metric is Hodge for a flag tie if $\partial$ is the complement of the interior and the matrices $G_{i,\tau}$ are the Gram matrices of the tie frames for the Hodge metric. It is conjugation invariant if $\partial$ and $r_W$ are invariant under complex conjugation of the coordinates and every line $h_{\tau,i}$ satisfies $h(\bar z) = h(z)$ off $\partial$.

**Theorem 10.6.4 (Base metric).** Assume the given statements. Let $M$ be a flag model of type $(p + q, p)$ with $p, q \geq 1$, let $\mathfrak{M}$ be a Hodge component over $M.x$ with a flag tie, and assume that $\mathfrak{M}$ is a cover of degree $d$ with a normal crossings boundary of dimension $n = \lvert\Psi\rvert p q$. Then there is a base metric of dimension $n$ on $M$ that is Hodge for the tie and conjugation invariant.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.BMx.baseMetricExists_of_given` (also `GlobalTheory.T.base_metric_exists_of_given`, a second name).

*Proof.* The given statements provide the moduli spaces at all levels, and with them the theory of the Hodge metric near the boundary.

Step 1: the resolution. The CM type is not empty. The boundary model is an arithmetic variety of dimension $n + 1$, and its boundary points are closed and stable under conjugation. This gives the log resolution $X_b$, the line bundle $L$ and the section $s$ with normal crossings, $\lVert s\rVert \leq 1$ and a conjugation invariant log distance. An atlas adapted to $s$ exists, and $\partial$ is closed.

Step 2: frames and bounds. There is a finite cover by open sets on which frames of $M$ are good. A cutoff function on each set and a global height identity bound the Hodge Gram matrices of the tie frames by a power of $r_W$; the constants are summed into one constant. A comparison of frames bounds the gradient.

Step 3: lines and periods. The resolution is integrable for the Hodge metric, which gives the lines $h_{\tau,i}$, their degrees, the induced metrics and their conjugation invariance. Near each point off $\partial$ there are local holomorphic period maps whose Gram matrices are the block matrices $G_{i,\tau}$ built from the base Gram matrices, and a lower height estimate gives a point where a period map is an immersion.

Step 4: assembly. The matrices $G_{i,\tau}$ are block diagonal and positive definite. The Gram matrix of the $W$ frame and the dual Gram matrix of the $\Omega$ frame are the two blocks, which is the Hodge property. The conjugation invariance of $\partial$ follows from that of the boundary points. $\square$

**Remark 10.6.5 (Formalization).** Both second names only restate their theorems (`Development/AutomorphicSpectrum/Proofs/MetricProofs/FlagModelExistsOfGivenStatement.lean` and `BaseMetricExistsOfGivenStatement.lean`). The statements are the propositions `FlagModelExists` and `BaseMetricExists` of `Development/AutomorphicSpectrum/Statements/MetricStatements/ExistsFlagModelBaseMetric.lean` (lines 66 and 95). Flag models are defined in `Definitions/MetricPeriods/GenericBlockMatrixIsBlockDiag.lean:382`, flag ties and the Hodge property in `Definitions/MetricPeriods/FiniteEtaleSurjectiveOfPullback.lean` (lines 402 and 439), base metrics in `Definitions/MetricPeriods/IsPeriodOn.lean:19`, and the given statements in `Definitions/DivisibilityTowers/GoodOrigin.lean:67`. In the proof of the flag model (`FlagModelExistsOfGiven.lean:34`) the given statements are introduced as an unnamed hypothesis at line 35 and never used. Four lemmas there have names that do not match their statements: `hodgeCpt_frame_order_bound` gives that the base coordinates are an arithmetic variety, `hodgeCpt_frame_unit_criterion` gives the dimension of part 3, `hodgeCpt_frame_generic_rank` gives the transfer of the normal crossings boundary, and `hodgeCpt_frame_degree_formula` gives that a scheme is normal (their statement files `HodgeCptFrame*Statement.lean`, line 9). In the proof of the base metric (`BaseMetricExistsOfGiven.lean:115`) the lemma that produces the resolution, the section and the normal crossings data is named `lowerBound_height_on_boundary` (line 130), the lemma that produces the lines and their conjugation invariance is named `flagModel_resolution_integrability` (line 159), and the lemma that produces the immersion point is named `flagModel_height_lower_estimate` (line 168). I did not unfold the lemmas behind the steps of either proof; the steps follow their statements and the order in which the proofs use them.
