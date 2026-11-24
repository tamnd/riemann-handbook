---
title: The head letter, the chart equations and the top lift
decls:
  - Formalism.FourierDecayAlt.P.CutHL.headLetter_of_minusPos
  - Formalism.FourierDecayAlt.P.CutHL.head_letter_of_minus_positive
  - Formalism.FourierDecayAlt.P.head_letter_identity
  - Formalism.FourierDecayAlt.P.z_only_of_levi_curve
  - Formalism.FourierDecayAlt.P.z_only
  - Formalism.FourierDecayAlt.P.CutHB.headBridge_of_rest
  - Formalism.FourierDecayAlt.P.head_germ_smooth_extension
  - Formalism.FourierDecayAlt.P.head_jacquet_of_letter_and_head
  - Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.chartEqs_of_capJoints
  - Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.chart_equations_holds
  - Formalism.FourierDecayAlt.P.top_lift_exists
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The head letter, the chart equations and the top lift

A word of letters acts on the radial space through the frames of the [word frames](/entry/plus-letter-maps-frames/). This section follows the action of a word through the level tower and back to the group. First, the head letter identity: at a point of the form $m(\operatorname{diag}(Z, \tau), \gamma)$, one letter at level $j + 1$ is a first order operator in the variable $\tau$ applied to the letter at level $j$ (compare the [chain step](/entry/chain-descent-relation/)). Second, the letter at level $j$ acts only through the variable $Z$. Together with a bridge that writes the coefficients of a place as integrals of such functions, these give the head Jacquet identity. Third, the chart equations say that a coefficient that is an eigenfunction of the Capelli operators satisfies, in a chart, a system of differential equations whose characteristic set is controlled by nilpotent elements. Last, the top lift turns the action of a word into a differential operator on the group, with a bound on its order. All results are used in the step [HypsAlt is nonempty](/step/nonempty-hyps/).

### The setting at level $j$

Fix $k, r$, a level $j$ with $j + 1 \le r$, and points $z, z'$ of the middle block. For a matrix $Z$ of size $j$, a number $\tau \in \mathbb C$ and $\gamma \in G_V(r - j - 1)$ put
$$x_0(Z, \tau, \gamma) = m\bigl(\operatorname{diag}(Z, \tau), \gamma\bigr),$$
the block map applied to the matrix of size $j + 1$ with blocks $Z$ and $\tau$. Let $D_l$ be the leading minors and $G_f$ the function of the [top unipotent integral](/entry/top-unipotent-integral/). The *domain at level $j$* is the open set where $D_j \ne 0$, $D_{j+1} \ne 0$ and $G_f > 0$. For $a \in \mathbb C^j$ let $n_L(a)$ be the left unipotent element of level $j$ attached to $a$; we do not unfold its matrix here.

**Definition 1.14.1 (The rules at level $j$).** Let $D$ be an open subset of the domain at level $j$ and let $\Phi$ be a function on $D$ with values in a normed space. Then $\Phi$ *satisfies the rules* if it is smooth on $D$ at level $0$, if $D$ is stable under right translation by the unipotent group $N$ and $\Phi(g n) = \psi_{z'}(n) \Phi(g)$, and if $D$ is stable under left translation by the elements $n_L(a)$ and $\Phi(n_L(a) g) = \psi_z(n_L(a)) \Phi(g)$.

For a letter $l$ (a sign and a real point $Y$), a level $i$ and a component $e \in \{0, 1\}$, let $v^{(i)}_{l, e}\Phi$ be the component $e$ of the action of the letter $l$ at level $i$ on $\Phi$. Put $\kappa_j = (r - j) + k/2$.

### The head letter identity

**Theorem 1.14.2 (Head letter identity).** Let $j + 1 \le r$, let $z, z'$ lie in the middle block, let $D$ be an open subset of the domain at level $j$, and let $\Phi$ satisfy the rules on $D$. Let $\det Z \ne 0$, $\tau \ne 0$, $\gamma \in G_V(r - j - 1)$ and $x = x_0(Z, \tau, \gamma) \in D$. Then for every real $Y$, writing $v^{(i)}_{\pm, e}$ for the letter $(\pm, Y)$,
$$\begin{aligned} v^{(j+1)}_{+, 0}\Phi(x) &= (Y + \kappa_j)\, v^{(j)}_{+, 0}\Phi(x) + \tau \partial_\tau v^{(j)}_{+, 0}\Phi(x) - \tau\, v^{(j)}_{+, 1}\Phi(x),\\ v^{(j+1)}_{+, 1}\Phi(x) &= \tau^{-1}\, v^{(j)}_{+, 0}\Phi(x),\\ v^{(j+1)}_{-, 0}\Phi(x) &= (Y - \kappa_j)\, v^{(j)}_{-, 0}\Phi(x) - \bar\tau \partial_{\bar\tau} v^{(j)}_{-, 0}\Phi(x) - \bar\tau\, v^{(j)}_{-, 1}\Phi(x),\\ v^{(j+1)}_{-, 1}\Phi(x) &= \bar\tau^{-1}\, v^{(j)}_{-, 0}\Phi(x). \end{aligned}$$
Here $\partial_\tau$ and $\partial_{\bar\tau}$ are the Wirtinger derivatives of $\tau \mapsto v^{(j)}\Phi(x_0(Z, \tau, \gamma))$.

Lean: `Formalism.FourierDecayAlt.P.CutHL.headLetter_of_minusPos` (with the inputs as hypotheses), `Formalism.FourierDecayAlt.P.CutHL.head_letter_of_minus_positive` (also `Formalism.FourierDecayAlt.P.head_letter_identity`, a second name).

*Proof.* The plus lines are proved from five facts at the base point $x_0$: the left rule at a level point, the torus action at $x_0$, the star rule at $x_0$, the star of the torus action, and the identities for the plus letter in its positive and zero components. The minus lines come from the identities for the minus letter. Those for the zero component are proved directly. Those for the positive component follow from the normal forms at the base point, the leading minors at the base point, the conjugate action rule and the conjugate torus direction. $\square$

### The letter acts through $Z$

**Theorem 1.14.3 (The letter acts only through $Z$).** Let $j + 1 \le r$, let $z, z'$ lie in the middle block, let $l$ be a letter and $e$ a component. There is a linear operator $A$ on functions of $j \times j$ matrices with the following properties. First, $A$ commutes with parameters: for every open set $U$ of pairs $(\tau, Z)$ with $\det Z \ne 0$ and every family $\kappa_\tau(Z)$ smooth on $U$, the family $A\kappa_\tau$ is smooth on $U$, and $A$ commutes with $\partial_\tau$ and $\partial_{\bar\tau}$. Second, for every open $D$ in the domain at level $j$, every $\Phi$ smooth on $D$ at level $0$, and all $Z, \tau, \gamma$ with $\det Z \ne 0$, $\tau \ne 0$ and $x_0(Z, \tau, \gamma) \in D$,
$$v^{(j)}_{l, e}\Phi\bigl(x_0(Z, \tau, \gamma)\bigr) = A\bigl(Z' \mapsto \Phi(x_0(Z', \tau, \gamma))\bigr)(Z).$$

Lean: `Formalism.FourierDecayAlt.P.z_only_of_levi_curve` (with the inputs as hypotheses), `Formalism.FourierDecayAlt.P.z_only`.

*Proof.* The letter at level $j$ is built from right invariant derivatives of level $j$. At the point $x_0$ these are derivatives along a curve in the Levi factor of the block of size $j$, so they only move $Z$: this is the statement on Levi curves. The hermitian part of the letter is also a Levi operator. The operator $A$ is the expression of these derivatives in the coordinates of $Z$, with coefficients given by the coefficient $\xi$ and its vector form; these are smooth, and the Wirtinger derivatives of a slice in $\tau$ commute with them. $\square$

### The head Jacquet identity

Let $p$ be a place, $F$ a compact coefficient, $w$ a cut word, $h$ a local point of size $j$, and $\gamma \in G_V(r - j - 1) \cap \Omega^+$. Let $J_F$ denote the coefficient of the slice of $F$ along a local point, as in the [slice induction](/entry/slice-induction-level/). For each component $e$ of the word let
$$\varphi_e(\tau) = J_F\bigl(\operatorname{sl}^{w, e}_h F\bigr)\bigl(m(\tau, \gamma)\bigr), \qquad \tau \ne 0,$$
be the coefficient at level $j$. Let $\mathcal B_j(w)$ be the one variable transform of the word $w$ with shift $\kappa_j$: it applies to the family $(\varphi_e)$, one letter at a time, the matrices of the head letter identity.

**Theorem 1.14.4 (Head Jacquet identity).** Assume the head letter identity and the bridge below. Then for every $t$ such that $h \cdot (1, t)$ is a local point and every component $e$,
$$J_F\bigl(\operatorname{sl}^{w, e}_{h \cdot (1, t)} F\bigr)(\gamma) = \mathcal B_j(w)(\varphi)_e(t).$$

Lean: `Formalism.FourierDecayAlt.P.head_jacquet_of_letter_and_head`

The *bridge* is the following statement. For the data above there are a measure space $(X, \mu)$, linear maps $\ell(x)$, matrices $Z(x)$ with $\det Z(x) \ne 0$, an open subset $D$ of the domain at level $j$, and functions $F_x$ that satisfy the rules on $D$, with $x_0(Z(x), \tau, \gamma) \in D$ for $\tau \ne 0$, such that the coefficient on the left is the integral over $x$ of $\ell(x)$ applied to the word function of $F_x$ at level $j + 1$ at $x_0(Z(x), t, \gamma)$, and the transform $\mathcal B_j(w)(\varphi)_e(t)$ is the integral of $\ell(x)$ applied to the transform of the level $j$ word functions of $F_x$.

*Proof.* By induction on the word, the head letter identity, the [fact that the letter acts only through $Z$](/entry/z-only/), and the closure of the rules under letters give the word identity: for each $F_x$, the word function at level $j + 1$ at $x_0(Z(x), t, \gamma)$ is the transform $\mathcal B_j(w)$ of the word functions at level $j$. The bridge writes both sides of the claim as integrals over $x$ of $\ell(x)$ applied to the two sides of the word identity. $\square$

**Theorem 1.14.5 (The bridge).** The bridge holds. It follows from three statements: the properness of the domain in the left variables, the smoothness of the word functions under the partial Bessel integral, and the statement on the first side (which is proved from a positive and a zero part).

Lean: `Formalism.FourierDecayAlt.P.CutHB.headBridge_of_rest` (with the three statements as hypotheses), `Formalism.FourierDecayAlt.P.head_germ_smooth_extension`.

*Proof.* The bridge is assembled from the rules for the slice functions, the smoothness of the word functions, the smoothness of the curve $\tau \mapsto x_0(Z, \tau, \gamma)$, a support statement for the letters under the partial Bessel integral (which uses the properness of the domain), the vanishing of the side zero part (also from the properness), the side one statement, and the fact that the one variable letters pass under the integral. $\square$

### The chart equations

Let $n = 2r + k + 1$. A function $u$ on matrices *satisfies the group equations* if it is of class $C^n$ on $\Omega^+$ at level $0$, if it is an eigenfunction (on the domain of $G_f > 0$ and nonvanishing minors) of the right and of the left invariant derivatives along the Lie algebra of $N$, of the left Capelli elements along every frame of $z$ and of the right Capelli elements along every frame of $z'$, and of the operators of the Casimir family $C(Y)$ for every real $Y$.

**Theorem 1.14.6 (Chart equations).** Let $k \ge 1$, let $z, z'$ lie in the middle block with $T(z), T(z') > 0$. Let $O \subseteq \mathbb R^d$ and $U$ be open, let $\kappa : O \to U$ be smooth with $\kappa(O) \subseteq G_V \cap \Omega^+$, and let $\Phi$ be smooth on $U$ with $\Phi(\kappa(x)) = x$ on $O$, and $\Phi(g) \in O$, $\kappa(\Phi(g)) = g$ for $g \in U \cap G_V$. Let $u$ satisfy the group equations. Then there is a finite family $(P_j)$ of differential operators on $O$ with smooth coefficients and of order at most $n$ such that $u \circ \kappa$ is $C^n$ on $O$, $P_j(u \circ \kappa) = 0$ for every $j$, and the following holds. If $x \in O$ and $\xi \ne 0$ is a common zero of all principal symbols of the $P_j$ at $x$, then there is a nonzero nilpotent $\Xi$ in the Lie algebra of $G_V$ with
$$\operatorname{Re}\operatorname{tr}(\Xi X) = 0 \quad (X \in \mathfrak u_W(z) \cup \mathfrak n), \qquad \operatorname{Re}\operatorname{tr}\bigl(\Xi\, \kappa(x) X \kappa(x)^{-1}\bigr) = 0 \quad (X \in \mathfrak u_W(z') \cup \mathfrak n).$$

Lean: `Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.chartEqs_of_capJoints` (with three statements on Capelli words as hypotheses), `Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.chart_equations_holds`.

*Proof.* Each eigen equation in the group equations has the form $(D - c) u = 0$ with $D$ a left or right invariant operator, and its pull back by the chart $\kappa$ is an equation on $O$ with smooth coefficients; these are the $P_j$. The three statements on Capelli words (a general, a right and a left one) express the Capelli elements as words in the generators, and with eleven further inputs they give the Capelli words for all frames. Nineteen further inputs then give the order bound and the statement on the common zeros of the symbols. We did not unfold these inputs. $\square$

### The top lift

Let $(X, \mu, L, \mathrm{st}, l_0)$ be a normal form datum with $1 \le l_0 \le k$. For a cut word $w$, the frame of the word gives an operator $F_w b_w$ on the radial space, where $b_w$ collects the letters, and for a component $e$ the vector $(F_w b_w \Phi_1)_e$, where $\Phi_1$ is the first state vector of a radial function $\Phi$.

**Theorem 1.14.7 (Top lift).** There is a constant $C_b \ge 0$ with the following property. For every place and every normal form datum $(X, \mu, L, \mathrm{st}, l_0)$ with $1 \le l_0 \le k$, there is a family $\Theta$ of operators $\Theta(w, e)$ on functions on $G_V$ such that:

1. for every cut word $w$, every compact coefficient $F$, every radial function $\Phi$ of $F$, and every component $e$, the vector $(F_w b_w \Phi_1)_e$ is the radial function of $\Theta(w, e) F$;
2. for every cut word $w$ and component $e$, the operator $\Theta(w, e)$ is a differential operator in the class $DD^+$, with fibre functions that obey the fibre bound, of order $o \le C_b\, |w|\, n$ and with polynomial degree $\kappa \le C_b (r + 1)\, o$, and $\Theta(w, e) F = D F$ on the domain of the class.

Lean: `Formalism.FourierDecayAlt.P.top_lift_exists`

*Proof.* The proof takes $C_b = 11$. Say that an element of the operator algebra of the radial space *lifts* if it is the radial form of a differential operator in $DD^+$ with bounded order and degree. The proof builds a lift system from the algebraic facts about the actual datum, the closure of lifts under the algebra operations, and the lifts of the function operators, of the elements $x(Y)$ and of the Capelli operators. Polynomial closure then gives a lift of the frame and the letters of every cut word, and $\Theta(w, e)$ is the lifted operator. $\square$

**Remark 1.14.8 (Formalization).** Each result here is a pair: an implication from named inputs and its application to proved inputs. We did not unfold the inputs (the Levi curve statement, the properness of the domain, the side one statement, the three statements on Capelli words, the class $DD^+$ and the fibre bound), nor the letter operators $v^{(i)}_{l, e}$ and the transform $\mathcal B_j(w)$; the statements above give them by their role. The constant $C_b = 11$ of the top lift is fixed in the proof.
