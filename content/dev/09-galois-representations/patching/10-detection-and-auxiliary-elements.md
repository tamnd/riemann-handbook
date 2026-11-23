---
title: Detection and the choice of auxiliary elements
decls:
  - UpperTheory.V.Pa.detection
  - UpperTheory.V.Pa.choice
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Detection and the choice of auxiliary elements

Both Selmer bounds need a finite set $\{\sigma_1, \dots, \sigma_q\}$ of group elements. The first order bound needs it to detect the dual classes, and both bounds need the characteristic polynomials of $\rho(\sigma_j)$ to split with distinct roots. The Taylor-Wiles places are then chosen, by the Chebotarev density theorem, with Frobenius elements close to the $\sigma_j$. This section proves that such a set exists, and that it can be chosen at once for finitely many points after a finite extension of their coefficients. For the background see [decomposition groups and Frobenius elements](/learn/galois-representations/#decomposition-groups-inertia-and-frobenius) and [patching](/learn/deformations-patching/#taylor-wiles-kisin-patching).

### Frames

The results of this section hold for a *frame*. A frame has the same structure as a global datum: a compact totally disconnected group $\Gamma$, a character $\eta$ with open kernel $\Gamma_0$, an element $c$, a character $\varepsilon$ to $\mathbb{Z}_l^\times$, local groups with maps to $\Gamma_0$, and in addition an auxiliary subgroup $D_0$ and a subgroup $G' \subseteq \Gamma_0$. Points of rank $n$, bases of odd classes, the twisted dual cocycles $\mathrm{TwZ}$ and the functionals $\ell_\sigma$ are defined for a frame as in the section on first order Selmer bounds. Recall that $\ell_\sigma(z)$ is the $h$ component of $\operatorname{tr}(z(\sigma)\rho_1(\sigma))$, and that a set $S$ detects the basis $\kappa$ if every $z \in \mathrm{TwZ}$ with $\ell_\sigma(z) = 0$ on $S$ has a multiple $t^s z$ that is a twisted coboundary.

A point $x$ with ring $A = K[[t]]$ satisfies condition $\mathrm{N}_3$ if every open subset of $\Gamma_0$ that meets $G'$ contains some $\sigma \in G'$ for which the characteristic polynomial of $\rho(\sigma)$ is separable over the fraction field of $A$.

An *extension* of a point $x$ is a point $x'$ of the same rank with an injective, local and finite ring map $j \colon A \to A'$ such that $\rho' = j \circ \rho$, the integers $a$ agree, and the local characters $\psi'_{v,i}$ are the images of the $\psi_{v,i}$.

### Detection by a dense set

**Theorem 7.10.1 (Detection).** Let $l \ne 2$ and let $F$ be a frame with some $g \in \Gamma_0$ such that $\varepsilon(g) \not\equiv 1 \bmod l$. Let $x$ be a point of rank $n$ and $\kappa$ a basis of odd classes. Let $S \subseteq G'$ with $G' \subseteq \overline{S}$. Then $S$ detects $\kappa$.

Lean: `UpperTheory.V.Pa.detection`.

*Proof.* There are two steps.

First, $G'$ itself detects $\kappa$. This is the main input, and we give it in outline. Over the fraction field of $A$, a twisted dual cocycle $z$ with $\ell_\sigma(z) = 0$ for all $\sigma \in G'$ pairs to zero, under the trace pairing, with every value of the first order thickening $\rho_1$ on $G'$. The point spans the even matrices over $\rho(G')$ up to a power of $t$, and the twist by $\varepsilon$ is nontrivial modulo the odd prime $l$. These two facts let one solve for a matrix $Y$ over the fraction field with $z(g) = \varepsilon(g)\rho_1(g) Y \rho_1(g)^{-1} - Y$. Clearing the denominators of $Y$ gives a power of $t$ with $t^s z$ a twisted coboundary over $A$.

Second, for $z \in \mathrm{TwZ}$ the set $\{\sigma \in \Gamma_0 : \ell_\sigma(z) = 0\}$ is closed. Indeed $z$ is continuous for the $t$-adic topology, and so is $\sigma \mapsto \rho_1(\sigma)$, so $\sigma \mapsto \ell_\sigma(z)$ is locally constant modulo each power of $t$.

Now let $z \in \mathrm{TwZ}$ vanish under $\ell_\sigma$ for all $\sigma \in S$. The closed set where $\ell_\sigma(z) = 0$ contains $S$, so it contains $\overline{S} \supseteq G'$. By the first step $t^s z$ is a twisted coboundary for some $s$. $\square$

The hypothesis $S \subseteq G'$ is not needed for the argument. Only the density of $S$ in $G'$ matters.

### Finite detecting sets with split eigenvalues

**Theorem 7.10.2 (Choice of auxiliary elements).** Let $l \ne 2$ and let $F$ be a frame whose group $\Gamma$ satisfies the $\Phi$ condition and has some $g \in \Gamma_0$ with $\varepsilon(g) \not\equiv 1 \bmod l$. Let $x_0, \dots, x_h$ be points of rank $n$ that satisfy $\mathrm{N}_3$. Then there are $q \in \mathbb{N}$, elements $\sigma_1, \dots, \sigma_q \in G'$, and for each $i$ an extension $x'_i$ of $x_i$, a basis $\kappa^{(i)}$ of odd classes of $x'_i$ and a family $\alpha^{(i)}$, such that:

1. all residue fields of the $x'_i$ have the same number of elements;
2. $\{\sigma_1, \dots, \sigma_q\}$ detects $\kappa^{(i)}$ for each $i$;
3. for each $i$ and $a$, the characteristic polynomial of $\rho'_i(\sigma_a)$ is $\prod_b (X - \alpha^{(i)}_{a,b})$ with $b \mapsto \alpha^{(i)}_{a,b}$ injective.

Lean: `UpperTheory.V.Pa.choice`.

*Proof.* Let $S$ be the set of $\sigma \in G'$ such that the characteristic polynomial of $\rho_i(\sigma)$ is separable over the fraction field for every $i$. A density lemma shows that condition $\mathrm{N}_3$ for the points $x_0, \dots, x_h$ gives $G' \subseteq \overline{S}$.

By the $\Phi$ condition each $x_i$ has a basis $\kappa_i$ of odd classes. By the detection theorem $S$ detects each $\kappa_i$.

The $\Phi$ condition also gives a finiteness lemma: if a set detects a basis, then some finite subset of it does. Choose finite $T_i \subseteq S$ that detect $\kappa_i$, and enumerate their union as $\sigma_1, \dots, \sigma_q$. Detection is monotone in the set, so $\{\sigma_1, \dots, \sigma_q\}$ detects every $\kappa_i$, and the $\sigma_a$ lie in $S \subseteq G'$.

For each $i$ the characteristic polynomials of the $\rho_i(\sigma_a)$ are separable. A finite extension of the coefficient field splits them, and then their roots in $A'$ are distinct. More precisely, there is $d_i \ne 0$ such that for every $D \ne 0$ divisible by $d_i$ there is an extension $x'$ of $x_i$ with residue field of $l^D$ elements, a basis of odd classes of $x'$ detected by $\{\sigma_a\}$, and split characteristic polynomials with distinct roots. Take $D = \prod_i d_i$. Then all the $x'_i$ have residue fields with $l^D$ elements. $\square$

The common residue field in item 1 is needed later. The patching argument puts several points on one universal ring, and their Selmer bounds are compared in powers of one number $\#K$.

**Remark 7.10.3 (Formalization).** In `detection` ([Detection.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/AutomorphicDetection/Detection.lean#L8)) the hypothesis $S \subseteq G'$ is bound to `_` and never used. The step that $G'$ detects is `Det.detAsm` in [DetAsm.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/DeterminantPadicFree/DetAsm.lean#L160). Its proof goes through `Det.detFr` and `Det.detAlg`, which we have not unfolded, so the first step of our proof is a summary of the mathematics and not a line by line account. The closedness is `Det.ellClosed`, the density is `Det.omDense`, the existence of a basis is `Det.kapEx`, the finite subset is `Det.detFin`, and the coefficient extension is `Det.onePt`. In [Choice.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/AutomorphicDetection/Choice.lean#L14) the monotonicity of detection is the private lemma `detects_mono`. The statements `Detection` and `Choice` are in [PatchedSupportCompletions.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/PatchedSupportCompletions.lean#L215).
